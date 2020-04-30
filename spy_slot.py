import datetime
import requests
import time
import argparse
import os
import json

def			windows_notify(title, content) :
	os.system('powershell.exe New-BurntToastNotification -Text \\"' + title + '\\" , \\"' + content + '\\"');

#def			debian_notify() :
#	pass

#def			osx_notify() :
#	pass

### Process function
#

def			process_spy_slot(browser_session, os_notifier) :
	query_frequence		= 10
	today				= datetime.date.today()
	url					= "https://projects.intra.42.fr/projects/" + args.project + "/slots.json"
	cookies				= {'_intra_42_session_production' : browser_session}
	params				= {
		'start' : str(today),
		'end':str(today + datetime.timedelta(days=args.days))
	}

	os_notifier("Spy slot :", "Is running")
	while True :
		response	= requests.get(url, params=params, cookies=cookies)
		data		= json.loads(response.content)

		if len(data) :
			os_notifier("Spy slot :", "One slot is available. Quick quick quick!")
		else :
			print(datetime.datetime.now().time(), 'No correction available')
		time.sleep(query_frequence)
	os_notifier("Spy slot :", "Spy slot ended")

### Script start
#

parser = argparse.ArgumentParser()

# Required
parser.add_argument("-p", "--project", help="project")
parser.add_argument("-s", "--session", help="session")

# Optional
parser.add_argument("-d", "--days", help="number of days from today", default=1)
parser.add_argument("-f", "--from", help="from hour", default=5)
parser.add_argument("-t", "--to", help="to hour", default=23)

args = parser.parse_args()

if (not args.project) :
	print('Please give a projectname  with -p, --project option')
	exit(1)
if (not args.session) :
	print('Please give a session id with -s, --session option')
	exit(1)

#process_spy_slot(browser_session = chrome_session(cookie_path), os_notifier = windows_notify);
process_spy_slot(browser_session = args.session, os_notifier = windows_notify);
