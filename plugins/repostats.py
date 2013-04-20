import requests
from baseplugins import BasePlugin
from baseplugins import add_help_text
import json

class RepoStatsPlugin(BasePlugin):

    def __init__(self):
        add_help_text(';github username reponame  shows watchers and stars for this project')
        self.commands = ((self.getRepoStats, {'startswith':'github '}),)

    def getRepoStats(self, channel, msg):
        params = msg.split()
        if len(params) == 3:
            stats = self.getGitHubStats(params[1], params[2])
            if(stats != None):
                self.bot.msg(channel, stats)
                return True
        return False

    def getGitHubStats(self, username, repo_name):
        r = requests.get('https://api.github.com/repos/%s/%s' % (username, repo_name))
        if(r.ok):
            repo = json.loads(r.text or r.content)
            msg = 'watchers: '+str(repo['watchers'])
            msg += '\nforks: '+str(repo['forks'])
        else:
            msg = None
        return msg
