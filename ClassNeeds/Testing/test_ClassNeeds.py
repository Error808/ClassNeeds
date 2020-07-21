'''

ClassNeeds testing script

'pip install nose2'
'nose2 -v' to run

'''

import os
import unittest
from ClassNeeds import app, db, updateRatingsTableClasses # code from module you're testing

# I (Jordan) set up a local postgres db
LOCAL_DB_URI = 'postgres://postgres:test1234@localhost:5432' # change this as necessary

class BasicTests(unittest.TestCase):
 
    ############################
    #### setup and teardown ####
    ############################
 
    # executed prior to each test
    def setUp(self):
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
    
    # ClassNeeds (main page) -------------------------------------
    ''' Tests that the main page returns a 200 status code. '''
    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    # SignUp -------------------------------------
    ''' Tests for signing up an account with the same email. '''
    def test_SignUp_invalid_same_email(self):
        response = self.SignUp('jotywong@ucsc.edu', 'abcd')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Signed up successfully, please sign in.', response.data)

        response = self.SignUp('jotywong@ucsc.edu', 'abcd') # second time, same email
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'This email address already exists!', response.data)

    ''' Tests for signing up an account. '''
    def test_SignUp_valid(self):
        response = self.SignUp('jotywong@ucsc.edu', 'abcd')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Signed up successfully, please sign in.', response.data)

    # SignIn -------------------------------------
    ''' Tests for signing in when already signed in. '''
    def test_SignIn_invalid_twice(self):
        self.SignUp('jotywong@ucsc.edu', 'abcd')
        self.SignIn('jotywong@ucsc.edu', 'abcd')
        response = self.SignIn('jotywong@ucsc.edu', 'abcd') # 2nd sign in
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'You are already signed in!', response.data)

    ''' Tests for an invalid email. '''
    def test_SignIn_invalid_email(self):
        self.SignUp('jotywong@ucsc.edu', 'abcd')
        response = self.SignIn('jotywongggggggg@ucsc.edu', 'abcd') # wrong email
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Email address or password is incorrect.', response.data)

    ''' Tests for an invalid password. '''
    def test_SignIn_invalid_pw(self):
        self.SignUp('jotywong@ucsc.edu', 'abcd')
        response = self.SignIn('jotywong@ucsc.edu', 'abcddddddddddddddddddddd') # wrong pw
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Email address or password is incorrect.', response.data)

    ''' Tests for signing in successfully. '''
    def test_SignIn_valid(self):
        self.SignUp('jotywong@ucsc.edu', 'abcd')
        response = self.SignIn('jotywong@ucsc.edu', 'abcd')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Signed in successfully.', response.data)

    # SignOut -------------------------------------
    ''' Tests for signing out when not already signed in. '''
    def test_SignOut_invalid_not_signed_in(self):
        response = self.SignOut()
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'You are not signed in!', response.data)

    ''' Tests for signing out successfully. '''
    def test_SignOut_valid(self):
        self.SignUp('jotywong@ucsc.edu', 'abcd')
        self.SignIn('jotywong@ucsc.edu', 'abcd')
        response = self.SignOut()
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'You signed out successfully.', response.data)

    # Classes -------------------------------------
    ''' Tests that an anonymous user cannot see classes. '''
    def test_Classes_invalid_anon(self):
        response = self.app.get(
            '/Classes',
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Please sign in or sign up first :)', response.data)

    ''' Tests that a good http response is returned for CSE 101. (POST) '''
    def test_Classes_valid_POST_CSE_101(self):
        self.SignUpAndSignIn('jotywong@ucsc.edu', 'abcd')
        response = self.app.post(
            '/Classes',
            data=dict(classChoose='CSE 101'),
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)

    ''' Tests for correct response from an unknown class. (POST) '''
    def test_Classes_invalid_POST_unknown_class(self):
        self.SignUpAndSignIn('jotywong@ucsc.edu', 'abcd')
        response = self.app.post(
            '/Classes',
            data=dict(classChoose='CSE 10111111111111'), # invalid class
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Could not find the specified class.', response.data)

    ''' Tests that a good http response is returned. (GET) '''
    def test_Classes_valid_GET(self):
        self.SignUpAndSignIn('jotywong@ucsc.edu', 'abcd')
        response = self.app.get(
            '/Classes',
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)

    # ClassDetails -------------------------------------


    # Ratings -------------------------------------
    ''' Tests that an anonymous user cannot see ratings. '''
    def test_Ratings_invalid_anon(self):
        response = self.app.get(
            '/Ratings',
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Please sign in or sign up first :)', response.data)

    ''' Tests that a good http response is returned for an upvote to CSE 101. (POST) '''
    def test_Ratings_valid_POST(self):
        updateRatingsTableClasses()
        self.SignUpAndSignIn('jotywong@ucsc.edu', 'abcd')
        response = self.app.get(
            '/Ratings',
            data=dict(classChoose='CSE 101', direction='up'),
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)

    ''' Tests that a good http response is returned. (GET) '''
    def test_Ratings_valid_GET(self):
        updateRatingsTableClasses()
        self.SignUpAndSignIn('jotywong@ucsc.edu', 'abcd')
        response = self.app.get(
            '/Ratings',
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)


    # Curriculum Charts -------------------------------------


    # About -------------------------------------


    # Profile -------------------------------------
    

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
            data=dict(user=email, passW=password),
            follow_redirects=True
        )
    
    def SignOut(self):
        return self.app.get(
            '/SignOut',
            follow_redirects=True
        )

    def SignUpAndSignIn(self, email, password):
        self.SignUp(email, password)
        self.SignIn(email, password)
 
if __name__ == "__main__":
    unittest.main()
