# AirReport

Scripts to collect and process the data from Airly sensors, then prepare report for website and send a notification (via e-mail).

## Airly API

In this project I use open data from [Airly](https://airly.org) air sensors to get air quality every hour. Airly lets to use their API to get data 100 times per day. It's necessary to make an account and generate API key for your project. You can read more about this API [here](https://developer.airly.org/en/docs).

## Python files

Below you can read about each one of my small python scripts.

### [save_data.py](save_data.py)

#### imports

First install all necessary libraries.

```python
import requests, sys, json, os, subprocess
from datetime import datetime
```

#### save_data

This is the main function and it prepares current date (`get_date()`), time(`get_time()`), places informations (`places` -> dictionary, where _key_ is the name and _value_ is an ID for Airly API) and `path` to directory to store new data. Then it uses a function **get_data(places[place])** for every place to connect with API and download raw data.

```python
def save_data():
    n = datetime.now()
    d = get_date(n)
    t = get_time(n)
    places = {'Lipowa': '11694', 'Cracow': '8973', 'BB': '11214', 'CPH': '86588'}
    path = '/path/to/data/' + d + '/'
    if not os.path.isdir(path):
        subprocess.call(["mkdir", path])
    sys.stdout = open(path + t, 'w')
    for place in places:
        print(place)
        print(get_data(places[place]))
    sys.stdout.close()
```

To use this script you have to put your _apikey_ in **my_headers** and add path to your directory for raw data (`'/path/to/data/'`).

### [make_report.py](make_report.py)

```
import json, typing
import matplotlib.dates as dts
import pandas as pd
import plotly.express as px
from os import walk
from datetime import datetime, date, timedelta
```

## Crontab
Mikrus: 30 8 * * 1 /usr/bin/python3.8 /path/to/script/send_report.py

RPI-1: 30 * * * * /usr/bin/python /path/to/script/save_data.py

RPI-2: 35 23 * * * date +\%F | xargs -I{} scp -P[port] -r /path/to/data/{} root@srv09.mikr.us:/path/to/data/
