### python-weather-cli

python-weather-cli is a command line interface to retrieve information on different locations. It allows for configuration of a default location. This allows to not pass a location argument each time. python-weather-cli uses Open Weather Map and pyowm to retrieve information, pyfiglet for text encoding and click for the cli creation.

### Installing

> $ pip install -U pyweathercli

### Configuration File

A configuration file can be located in the package file. The file is named under `config.json`. Below is the diagram.

```json
{
    "default_location": "",
    "api_key": ""
}
```

### Obtaining an OWM API Key

To obtain an OWM API Key, visit the link [here](https://openweathermap.org/). Click the login button. Then enter your credentials or sign up. You will be greeted with a landing page. On the middle navigation bar, click API Keys, and a `default` API Key will be shown. You can copy that or make one of your own. Once you obtain your API Key, set it using the `--apikey` flag during your first use. Example:

> $ weather --location "Los Angeles" --apikey "API KEY HERE"

### Use

# Setting a default location via the command line

> $ weather [-d or --default] "Location name"

This will edit the configuration file with a default location name. Doing this will alow the following usage.

```
$ weather
---------------------------------------------------------
  ____ _
 / ___| | ___  __ _ _ __
| |   | |/ _ \/ _` | '__|
| |___| |  __/ (_| | |
 \____|_|\___|\__,_|_|


Location: Los Angeles
Clear Sky
Sunrise Time: 2020-05-23 10:32:13+00
Sunset Time: 2020-05-24 00:40:06+00
Temperature: 66°F / 19°C
Heat Index: 66°F / 19°C
Humidity: 93%
Pressure: 32 barometers
Wind: 3mph / 5kph
Visibility Distance: 10m / 16km
---------------------------------------------------------
```

# Use without a default location

```
$ weather [--location or -l] "Location name"
---------------------------------------------------------
  ____ _
 / ___| | ___  __ _ _ __
| |   | |/ _ \/ _` | '__|
| |___| |  __/ (_| | |
 \____|_|\___|\__,_|_|


Location: Los Angeles
Clear Sky
Sunrise Time: 2020-05-23 10:32:13+00
Sunset Time: 2020-05-24 00:40:06+00
Temperature: 66°F / 19°C
Heat Index: 66°F / 19°C
Humidity: 93%
Pressure: 32 barometers
Wind: 3mph / 5kph
Visibility Distance: 10m / 16km
---------------------------------------------------------
```