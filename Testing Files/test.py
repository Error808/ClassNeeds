import unittest
from ClassNeeds import app # code from module you're testing

class testCases(unittest.TestCase):

    def testNoSignIn(self):
        '''Test case A. check for proper response if not signed in'''


if __name__ == "__main__":
    unittest.main() # run all tests