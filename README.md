# 	Spy slot

Please add start if you like it.

```
python .\spy_slot.py -p rainfall -s 010265afdc1f929384701c9a36522d4
```

### Get session_cookie

From your browser go to the intra connect to your Session. Througt the developer get the tools retrieve the session_id value. The key is `_intra_42_session_production`.

### Windows setup

Python3 is needed if it's not installed yet you should install it with `choco` package manager.

[chocolatey python3](https://chocolatey.org/packages/python3)

From powershell install `BurntToast` module (visit my gist [hear](https://gist.github.com/CallMarl/997bb9e31e2cd12b4cba7d1804f4c41b) for mor usual tools)

```
Install-Module BurntToast
```

Buid the environnement.

```
python3 -m venv env
.\env\Scripts\activate
pip install requests
```

Run the script.


### OSX setup

### Linux setup
