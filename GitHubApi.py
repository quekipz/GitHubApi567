"""
Kipsy Quevada
SSW-567-WS: SW Testing, Qual. Assur. & Maint
Fall 2018 | Professor Rich Kempinski
HW 04a: Develop with the Perspective of the Tester in mind
The goal of this assignment is to approach it as a developer who more
than anything else has the perspective of the tester in the front of their mind. 
AMDG
"""
#---------------------------------------------------------------------------

import requests
import json

def getReposAndCommits(user):
    """ Take as input a GitHub user ID. The output from the function will be a
    list of the names of the repositories that the user has, along with the
    number of commits that are in each of the listed repositories. """
    r = requests.get('https://api.github.com/users/' + user + '/repos')
    repos = json.loads(r.content)
    if 'message' in repos: # message: Not found will appear in dict if user is invalid
        yield "Error: User not found. Please try again."
    else:
        for rep in repos:
            c = requests.get('https://api.github.com/repos/' + user + '/' + rep['name'] + '/commits')
            commits = json.loads(c.content)
            yield "Repo: " + rep['name'] + " Number of commits: " + str(len(commits))