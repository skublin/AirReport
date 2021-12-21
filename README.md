# AirReport
Script to collect data from Airly sensors, process, prepare report for website and send notification (via e-mail).

## Crontab
Mikrus: 30 8 * * 1 /usr/bin/python3.8 /path/to/script/send_report.py

RPI-1: 30 * * * * /usr/bin/python /path/to/script/save_data.py

RPI-2: 35 23 * * * date +\%F | xargs -I{} scp -P[port] -r /path/to/data/{} root@srv09.mikr.us:/path/to/data/
