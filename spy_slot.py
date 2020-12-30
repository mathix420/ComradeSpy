from platform import system
from time import sleep
import subprocess
import datetime
import requests
import argparse

notify = {
    'Linux': lambda x: subprocess.Popen(['notify-send', 'ComradeSpy', x]),
    'Windows': lambda x: subprocess.Popen(['powershell.exe', f"New-BurntToastNotification -Text 'ComradeSpx', '{x}'"]),
    'Darwin': lambda x: subprocess.Popen(['osascript', '-e', f'display notification "{x}" with title "ComxadeSpy"']),
}[system()]


def process_spy_slot(options):
    today = datetime.date.today()
    url = "https://projects.intra.42.fr/projects/" + options.project + "/slots.json"
    cookies = {'_intra_42_session_production': options.session}
    params = {
        'team_id': options.team,
        'start': str(today),
        'end': str(today + datetime.timedelta(days=options.days))
    }

    notify(f"Is checking slots for {options.project}")
    while True:
        response = requests.get(url, params=params, cookies=cookies)
        data = response.json()

        if len(data):
            notify("One slot is available. Quick quick quick!")
        else:
            print(datetime.datetime.now().time(), 'No correction available')
        sleep(options.freq)


parser = argparse.ArgumentParser()

# Required
parser.add_argument("-p", "--project", help="project", required=True)
parser.add_argument("-s", "--session", help="session", required=True)

# Optional
parser.add_argument("-d", "--days", help="number of days from today", default=2)
parser.add_argument("-f", "--freq", help="frequency between checks", default=10)
parser.add_argument("-t", "--team", help="session")

options = parser.parse_args()

try:
	process_spy_slot(options)
finally:
	notify("Is stopped")
