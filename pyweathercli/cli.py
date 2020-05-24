import click
import pyowm
from pyfiglet import figlet_format
import json
import site
from pathlib import Path
import sys

path = Path(sys.modules[__name__].__file__).parents[0] / 'config.json'

with open(path) as cf:
    config = json.load(cf)

def write_location(location):
    with open(path, "w") as cf:
        json.dump({"default_location": f"{location}", "api_key": config["api_key"]}, cf)

def write_key(key):
    with open(path, "w") as cf:
        json.dump({"default_location": config["default_location"], "api_key": key}, cf)

@click.command(help="Returns weather information on a location using OWM.")
@click.option("--location", "-l", required=False, help="The location to retrieve information on.")
@click.option("--default", "-d", required=False, help="Use this flag to set a default location.")
@click.option("--apikey", "-k", required=False, help="Use this flag to set your OWM API Key.")
def weather(location: str=None, default: str=None, apikey: str=None):
    if default is not None:
        write_location(default)
    if location is None:
        if default is None:
            if config["default_location"] == '':
                return click.secho("Error: Location is a required argument whilst a default location is not set.", fg="red")
            else:
                location = str(config["default_location"])
        else:
            location = default

    if apikey is None:
        if config['api_key'] == '':
            return click.secho("Error: A API key was not provided", fg="red")
        else:
            key = config['api_key']
    else:
        write_key(apikey)
        key = apikey

    owm = pyowm.OWM(key)
    try:
        observation = owm.weather_at_place(location)
    except pyowm.exceptions.api_response_error.NotFoundError:
        return click.secho("Error: Location could not be found.", fg="red")

    weather = observation.get_weather()

    pressure = weather.get_pressure()["press"]
    humidity = weather.get_humidity()
    temp_celsius = round(weather.get_temperature('celsius')["temp"])
    temp_fahrenheit = round(weather.get_temperature('fahrenheit')["temp"])
    wind_kph = round(weather.get_wind()['speed'] * 3600 / 1000, 2)
    wind_mph = round(weather.get_wind()['speed'] / 0.44704, 2)
    detailed_weather  = weather.get_detailed_status()
    visibility = round(weather.get_visibility_distance() / 1000)
    visibility_miles = round(visibility * 0.62137)
    heat_index = weather.get_heat_index()
    sunrise = weather.get_sunrise_time("iso")
    sunset = weather.get_sunset_time("iso")

    click.secho("---------------------------------------------------------", fg="red")
    click.echo(figlet_format(weather.get_status()))
    click.echo(detailed_weather.title())
    click.echo(f"Location: {observation.get_location().get_name()}")
    click.echo(f"Sunrise Time: {sunrise}")
    click.echo(f"Sunset Time: {sunset}")
    click.echo(f"Temperature: {temp_fahrenheit}°F / {temp_celsius}°C")
    click.echo(f"Heat Index: {heat_index or temp_fahrenheit}°F / {heat_index or temp_celsius}°C")
    click.echo(f"Humidity: {humidity}%")
    click.echo(f"Pressure: {round(pressure ** .5)} barometers")
    click.echo(f"Wind: {round(wind_mph)}mph / {round(wind_kph)}kph")
    click.echo(f"Visibility Distance: {visibility_miles}m / {visibility}km")
    click.secho("---------------------------------------------------------", fg="red")