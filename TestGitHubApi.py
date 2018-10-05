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

import unittest
from GitHubApi import getReposAndCommits, yieldReposAndCommits
from unittest.mock import patch, MagicMock as Mock
import json

class TestGetReposAndCommits(unittest.TestCase):
    """ test getReposAndCommits function """
    
    # def testInvalidUser(self):
    #     results = list()
    #     for line in yieldReposAndCommits(''):
    #         results.append(line)
    #     self.assertEqual(results, ['Error: User not found. Please try again.'], 'Any invalid user results in error message.')
    
    # def testRichKempinski(self):
    #     results = list()
    #     for line in yieldReposAndCommits('richkempinski'):
    #         results.append(line)
    #     self.assertEqual(results, ['Repo: hellogitworld Number of commits: 30', 'Repo: helloworld Number of commits: 2', 'Repo: Mocks Number of commits: 3', 'Repo: Project1 Number of commits: 2', 'Repo: threads-of-life Number of commits: 1'], 'Richkempinski has 5 repos.')
    # Note: Originally included my own user 'quekipz' but realized that my commit count increases when I push the assignment, which fails the test.
    
    @patch('requests.get')
    def testInvalidUserMock(self, injectedMock):
        final_results = list()
        results = [Mock(), Mock()]
        results[0].json.return_value = {"message": "Not Found", "documentation_url": "https://developer.github.com/v3"}
        results[1].json.return_value = {"message": "Not Found", "documentation_url": "https://developer.github.com/v3"}
        injectedMock.side_effect = results
        for line in yieldReposAndCommits(''):
            final_results.append(line)
        self.assertEqual(final_results, ['Error: User not found. Please try again.'], 'Any invalid user results in error message.')

    @patch('requests.get')
    def testRichKempinskiMock(self, injectedMock):
        final_results = list()
        results = [Mock(), Mock(), Mock(), Mock(), Mock(), Mock()]
        results[0].json.return_value = [{"name": "hellogitworld"}, {"name": "helloworld"}, {"name": "Mocks"}, {"name": "Project1"}, {"name": "threads-of-life"}]
        results[1].json.return_value = [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}]
        results[2].json.return_value = [{}, {}]
        results[3].json.return_value = [{}, {}, {}]
        results[4].json.return_value = [{}, {}]
        results[5].json.return_value = [{}]
        injectedMock.side_effect = results
        for line in yieldReposAndCommits('richkempinski'):
            final_results.append(line)
        self.assertEqual(final_results, ['Repo: hellogitworld Number of commits: 30', 'Repo: helloworld Number of commits: 2', 'Repo: Mocks Number of commits: 3', 'Repo: Project1 Number of commits: 2', 'Repo: threads-of-life Number of commits: 1'], 'Richkempinski has 5 repos.')



if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()