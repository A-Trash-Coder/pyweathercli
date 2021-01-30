import json
import sys
from pathlib import Path

import click
import pyowm
from pyfiglet import figlet_format
import dateutil.parser


path = Path(sys.modules[__name__].__file__).parents[0] / "config.json"

with open(path) as cf:
    config = json.load(cf)


def write_location(location):
    with open(path, "w") as cf:
        json.dump({"default_location": f"{location}",
                   "api_key": config["api_key"]}, cf)


def write_key(key):
    with open(path, "w") as cf:
        json.dump(
            {"default_location": config["default_location"], "api_key": key}, cf)


@click.command(help="Returns weather information on a location using OWM.")
@click.option("--location", "-l", required=False, help="The location to retrieve information on.")
@click.option("--default", "-d", required=False, help="Use this flag to set a default location.")
@click.option("--api_key", "-k", required=False, help="Use this flag to set your OWM API Key.")
def weather(location: str = None, default: str = None, api_key: str = None):
    if default:
        write_location(default)
    if not location:
        if not default:
            if not config["default_location"]:
                return click.secho("Error: Location is a required argument whilst a default location is not set.", fg="red")
            else:
                location = str(config["default_location"])
        else:
            location = default

    if not api_key:
        if not config["api_key"]:
            return click.secho("Error: A API key was not provided", fg="red")
        else:
            key = config["api_key"]
    else:
        write_key(api_key)
        key = api_key

    owm = pyowm.owm.OWM(key)
    try:
        observation = owm.weather_manager().weather_at_place(location)
    except pyowm.commons.exceptions.NotFoundError:
        return click.secho("Error: Location could not be found.", fg="red")

    weather = observation.weather
    pressure = weather.pressure
    humidity = weather.humidity
    temp_celsius = round(weather.temperature("celsius")["temp"])
    temp_fahrenheit = round(weather.temperature("fahrenheit")["temp"])
    wind_kph = weather.wind("km_hour")
    wind_mph = weather.wind("miles_hour")
    detailed_weather = weather.detailed_status
    visibility = weather.visibility_distance
    heat_index = weather.heat_index
    sunrise = weather.sunrise_time(timeformat='date')
    sunset = weather.sunset_time(timeformat='date')

    click.secho(
        "---------------------------------------------------------", fg="red")
    click.echo(figlet_format(weather.status))
    click.echo(detailed_weather.title())
    click.echo(f"Location: {observation.location.name}")
    click.echo(f"Lon: {observation.location.lon}")
    click.echo(f"Lat: {observation.location.lat}")
    click.echo(f"Sunrise Time: {sunrise}")
    click.echo(f"Sunset Time: {sunset}")
    click.echo(f"Temperature: {temp_fahrenheit}°F / {temp_celsius}°C")
    click.echo(
        f"Heat Index: {heat_index or temp_fahrenheit}°F / {heat_index or temp_celsius}°C")
    click.echo(f"Humidity: {humidity}%")
    click.echo(f"Pressure: {pressure['press']} mb")
    click.echo(f"Wind: {round(wind_mph['speed'])}mph / {round(wind_kph['speed'])}kph")
    click.echo(f"Visibility Distance: {visibility}")
    click.secho(
        "---------------------------------------------------------", fg="red")
