from dotenv import load_dotenv
from slack import WebClient
from platform import system
from time import sleep
from os import getenv
import subprocess
import datetime
import requests
import argparse

load_dotenv()

if getenv('SLACK_TOKEN'):
    slack = WebClient(getenv('SLACK_TOKEN'))

notify = {
    'Linux': lambda x: subprocess.Popen(['notify-send', 'ComradeSpy', x]),
    'Windows': lambda x: subprocess.Popen(['powershell.exe', f"New-BurntToastNotification -Text 'ComradeSpx', '{x}'"]),
    'Darwin': lambda x: subprocess.Popen(['osascript', '-e', f'display notification "{x}" with title "ComxadeSpy"']),
}[system()]


def slack_message(options):
    url = f'https://projects.intra.42.fr/projects/{options.project}/slots?team_id={options.team}'
    slack.chat_postMessage(
        channel=options.slack_id,
        text=f'One slot is available for {options.project}.',
        attachments=[{
            "fallback": url,
            "color": "#BC0000",
            "attachment_type": "default",
            "actions": [{
                "type": "button",
                "text": "Check slots",
                "url": url
            }]
        }],
        username='Comrade Spy',
        icon_emoji=':sleuth_or_spy:'
    )

# Too spammy
# def open_in_browser(options):
#     subprocess.Popen([
#         'google-chrome',
#         f'https://projects.intra.42.fr/projects/{options.project}/slots?team_id={options.team}'
#     ])


def process_spy_slot(options):
    today = datetime.date.today()
    url = f'https://projects.intra.42.fr/projects/{options.project}/slots.json'
    cookies = {'_intra_42_session_production': options.session}
    params = {
        'team_id': options.team,
        'start': str(today),
        'end': str(today + datetime.timedelta(days=options.days))
    }

    if options.slack_id:
        slack.chat_postMessage(
            channel=options.slack_id,
            text=f'Spy slot strated!',
            username='Comrade Spy',
            icon_emoji=':sleuth_or_spy:'
        )

    notify(f'Is checking slots for {options.project}')
    while True:
        response = requests.get(url, params=params, cookies=cookies)
        data = response.json()


        if len(data):
            try:
                with open(f'slots-{options.project}.log', 'a+') as fp:
                    fp.write(str(data))
                    fp.write('\n\n'+'='*100+'\n\n')
            except:
                pass

            notify(f'One slot is available for {options.project}.')

            if options.slack_id:
                slack_message(options)
            # if options.open:
            #     open_in_browser(options)
        else:
            print(datetime.datetime.now().time(), 'No correction available')
        sleep(options.freq)


parser = argparse.ArgumentParser()

# Required
parser.add_argument('-p', '--project', help='project', required=True)
parser.add_argument('-s', '--session', help='session', required=True)

# Optional
parser.add_argument('-d', '--days', help='number of days from today', default=2, type=int)
parser.add_argument('-f', '--freq', help='frequency between checks', default=10, type=int)
# parser.add_argument('-o', '--open', help='open slots in browser', action='store_true')
parser.add_argument('--slack-id', help='send slack notifs to this conv id')
parser.add_argument('-t', '--team', help='session')

options = parser.parse_args()

try:
    process_spy_slot(options)
finally:
    notify('Is stopped')
