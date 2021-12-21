import requests, sys, json, os, subprocess
from datetime import datetime


def get_date(now):
    current_date = now.strftime("%Y-%m-%d")
    return current_date


def get_time(now):
    current_time = now.strftime("%H-%M-%S")
    return current_time


def connection(url, my_headers):
    response = requests.get(url, headers=my_headers)
    return response.json()


def jprint(selected_values):
    return json.dumps(selected_values, sort_keys=True, indent=4)


def get_data(idx):
    my_headers = {'apikey': '[Airly-apikey]'}
    url = 'https://airapi.airly.eu/v2/measurements/installation?installationId=' + idx
    raw = connection(url, my_headers)
    return jprint(raw['current']['values'])


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


if __name__ == '__main__':
    save_data()
