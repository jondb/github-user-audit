# Audit github users

Using a custom / forked version of pygithub with some hacks.

## install

```
git clone git@github.com:jondb/audit-tools.git
cd gh-user-audit
virtualenv penv
. penv/bin/activate
pip install ./PyGithub
touch creds.py
```

## configure

Copy this into a the file called creds.py at the root and update the user, personal access token and the organization.

```
class Creds(object):
	user = "xxxxxx"
	password = "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"
	organization = "zzzzzzzzzzzzzzzz"
	def __init__(self):
		pass
```

## run it
```
python audit.py
```

## results

the results are in a file called `output.csv`.
