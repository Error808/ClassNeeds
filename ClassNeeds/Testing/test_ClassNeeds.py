'''

ClassNeeds testing script

'pip install nose2'
'nose2 -v' to run

'''

import os
import unittest
from ClassNeeds import app # code from module you're testing

class BasicTests(unittest.TestCase):
 
    ############################
    #### setup and teardown ####
    ############################
 
    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

        # TODO: can I include this? this will reset the db every time
        # so the tests have the same baseline
        '''db.drop_all()
        db.create_all()'''
 
    # executed after each test
    def tearDown(self):
        pass
 
    ###############
    #### tests ####
    ###############
    
    # ClassNeeds (main page)
    ''' Tests that the main page returns a 200 status code. '''
    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    # Home (profile page? WIP (work in progress) )

    # SignUp
    ''' Tests for signing up an account. '''
    '''def test_valid_SignUp(self):
        response = self.SignUp('jotywong@ucsc.edu', 'abcd')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Signed up successfully, please sign in.', response.data)'''

    ''' Tests for signing up an account with the same email. '''

    # SignIn
    ''' Tests for signing in when already signed in. '''

    ''' Tests for an invalid email. '''

    ''' Tests for an invalid password. '''

    ''' Tests for signing in successfully. '''

    # SignOut
    ''' Tests for signing out when not already signed in. '''

    ''' Tests for signing out successfully. '''

    # Classes


    # Ratings


    # About

    ########################
    #### helper methods ####
    ########################

    def SignUp(self, email, password):
        return self.app.post(
            '/SignUp',
            data=dict(user=email, passW=password),
            follow_redirects=True
        )
    
    def SignIn(self, email, password):
        return self.app.post(
            '/SignIn',
            data=dict(email=email, password=password),
            follow_redirects=True
        )
    
    def SignOut(self):
        return self.app.get(
            '/SignOut',
            follow_redirects=True
        )
 
if __name__ == "__main__":
    unittest.main()
