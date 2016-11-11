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


# notes on hacks to pygithub

all changes to https://github.com/PyGithub/PyGithub/tree/a7eb09af049dbcc0d1c71b92abe3b71022b90eb9

Only changed file is https://github.com/PyGithub/PyGithub/blob/a7eb09af049dbcc0d1c71b92abe3b71022b90eb9/github/NamedUser.py

to add the fields for site_admin, and permissions to the user object that we get when we call repository.collaborators().
