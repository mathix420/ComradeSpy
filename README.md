# ComradeSpy

Be notified on new slot available.

```bash
python spy.py -p 'rainfall' -s '10265afdc1f929384701c9a36522d4'
```

## Setup slack notifications

You should add a `.env` file in the root folder.
```
├── .env
├── .gitignore
├── README.md
├── requirements.txt
└── spy.py
```
`.env`:
```
SLACK_TOKEN='xoxp-**************'
``` 

## Get session_cookie

From your browser go to [intra.42.fr](https://intra.42.fr/) connect to your Session. Througt the developer tools retrieve the cookie value. The key is `_intra_42_session_production`.

## Windows setup

From powershell install `BurntToast` module
```powershell
Install-Module -Name BurntToast
```

## OSX setup

Nothing special, just run `spy.py`.

## Linux setup

Nothing special too.
