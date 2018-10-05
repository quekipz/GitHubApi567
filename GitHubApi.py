"""
Kipsy Quevada
SSW-567-WS: SW Testing, Qual. Assur. & Maint
Fall 2018 | Professor Rich Kempinski
HW 05a: Isolate External Dependencies
In this assignment you will use a mocking package
to "mock" your program's external dependence on
GitHub, so that you can guarantee that your unit
tests will run consistently ever time you run them,
no matter how many times you run them, and no matter
what changes you make to your repos.
AMDG
"""
#---------------------------------------------------------------------------

import requests
import json

def getReposAndCommits(user):
    """ Take as input a GitHub user ID. The output from the function will be a
    list of the names of the repositories that the user has, along with the
    number of commits that are in each of the listed repositories. """
    results = []
    r = requests.get('https://api.github.com/users/' + user + '/repos')
    repos = r.json()
    if 'message' in repos: # message: Not found will appear in dict if user is invalid
        results.append(["Error", 0])
    else:
        for rep in repos:
            c = requests.get('https://api.github.com/repos/' + user + '/' + rep['name'] + '/commits')
            commits = c.json()
            results.append([rep['name'], str(len(commits))])
    return results

def yieldReposAndCommits(user):
    data_list = getReposAndCommits(user)
    if data_list[0][0] == "Error":
        yield 'Error: User not found. Please try again.'
    else:
        for item in data_list:
            yield "Repo: " + item[0] + " Number of commits: " + item[1]

# print(getReposAndCommits('richkempinski'))