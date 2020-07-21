'''

ClassNeeds testing script

'pip install nose2'
'nose2 -v' to run

'''

import os
import unittest
from ClassNeeds import app, db # code from module you're testing

# I (Jordan) set up a local postgres db
LOCAL_DB_URI = 'postgres://postgres:test1234@localhost:5432' # change this as necessary

class BasicTests(unittest.TestCase):
 
    ############################
    #### setup and teardown ####
    ############################
 
    # executed prior to each test
    def setUp(self):
        #print("setup")
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = LOCAL_DB_URI 
        self.app = app.test_client()
        db.drop_all()
        db.create_all()
 
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

    # SignUp
    ''' Tests for signing up an account. '''
    def test_valid_SignUp(self):
        #print("valid")
        response = self.SignUp('jotywong@ucsc.edu', 'abcd')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Signed up successfully, please sign in.', response.data)

        response = self.SignUp('jotywong@ucsc.edu', 'abcd') # second time, same email
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'This email address already exists!', response.data)

    ''' Tests for signing up an account with the same email. '''
    '''def test_invalid_SignUp(self):
        #print("invalid")
        response = self.SignUp('jotywong@ucsc.edu', 'abcd')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Signed up successfully, please sign in.', response.data)

        response = self.SignUp('jotywong@ucsc.edu', 'abcd') # second time, same email
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'This email address already exists!', response.data)'''

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


    # Curriculum Charts


    # About


    # Profile
    

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
