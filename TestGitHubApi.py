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

import unittest

from GitHubApi import getReposAndCommits

class TestGetReposAndCommits(unittest.TestCase):
    """ test getReposAndCommits function """
    def testInvalidUser(self):
        results = list()
        for line in getReposAndCommits(''):
            results.append(line)
        self.assertEqual(results, ['Error: User not found. Please try again.'], 'Any invalid user results in error message.')
    def testRichKempinski(self):
        results = list()
        for line in getReposAndCommits('richkempinski'):
            results.append(line)
        self.assertEqual(results, ['Repo: hellogitworld Number of commits: 30', 'Repo: helloworld Number of commits: 2', 'Repo: Project1 Number of commits: 2', 'Repo: threads-of-life Number of commits: 1'], 'Richkempinski has 4 repos.')
    def testQueKipz(self):
        results = list()
        for line in getReposAndCommits('quekipz'):
            results.append(line)
        self.assertEqual(results, ['Repo: helloworld Number of commits: 2', 'Repo: HW09 Number of commits: 3', 'Repo: triangle-classification Number of commits: 4', 'Repo: Triangle567 Number of commits: 7'], 'Quekipz has 4 repos.')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()