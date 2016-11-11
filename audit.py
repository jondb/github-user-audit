from github import Github
import csv
from creds import Creds as creds
import collections


class UserPerms(object):
	def __init__(self):
		self.repo_names = []
		# self.gh_repos = collections.defaultdict(set)
		self.gh_users_to_repos = collections.defaultdict(set)
		self.gh_users_repos_to_perms = collections.defaultdict(dict)

	def add(self, gh_repo, gh_user):
		if gh_repo.full_name not in self.repo_names:
			self.repo_names.append(gh_repo.full_name)
		# self.gh_repos_to_users[gh_repo.full_name].add(gh_user)

		self.gh_users_to_repos[gh_user.login].add(gh_repo.full_name)
		self.gh_users_repos_to_perms[gh_user.login][gh_repo.full_name] = gh_user

	def getUsers(self):
		user_perms = []
		for user_login in sorted(self.gh_users_to_repos.keys()):
			user_perms_row = [user_login]
			for repo_name in self.repo_names:
				gh_perms = self.gh_users_repos_to_perms[user_login].get(repo_name, None)
				if not gh_perms:
					user_perms_row.append('')
				else:
					perms = gh_perms.permissions
					if gh_perms.site_admin or perms['admin']:
						user_perms_row.append('RWA')
					elif perms['push'] and perms['pull']:
						user_perms_row.append('RW')
					elif perms['push']:
						user_perms_row.append('W')
					elif perms['pull']:
						user_perms_row.append('R')
					else:
						user_perms_row.append('?')
			user_perms.append(user_perms_row)
		return user_perms


if __name__ == '__main__':
	org = creds.get_organization

	g = Github(creds.user, creds.password)
	repos = g.get_organization(org).get_repos()
	active_repos = sorted(repos, key=lambda x: x.pushed_at, reverse=True)[:30]

 	repo_names = map(lambda x: x.full_name, active_repos)

 	user_p = UserPerms()

 	for repo in active_repos:
 		for user in repo.get_collaborators():
 			user_p.add(repo, user)

	with open('output.csv', 'wb') as csvfile:
		writer = csv.writer(csvfile, dialect='excel')
		writer.writerow(['User'] + repo_names)
		for row in user_p.getUsers():
 			writer.writerow(row)

