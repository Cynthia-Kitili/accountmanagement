import unittest
from user import User
from credentials import Credentials

class Testuser(unittest.TestCase):
    '''
    Test class that defines test for the user class behaviours.
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Cindy","fox12345")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly.
        '''
        self.assertEqual(self.new_user.username,"Cindy")   
        self.assertEqual(self.new_user.password,"fox12345") 

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into the user list.
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def tearDown(self):
        '''
        tearDown method that does clean up after each test has run.
        '''
        User.user_list = []    

    def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple user objects to our user_list.
        '''
        self.new_user.save_user()
        test_user = User("Test","fox12345")

        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a user from our user list.
        '''
        self.new_user.save_user()
        test_user = User("Test","fox12345")

        test_user.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)    

    def test_user_by_username(self):
        '''
        test to check if we can find a contact by username and display information"
        '''
        self.new_user.save_user()
        test_user = User("Test","fox12345")

        test_user.save_user()

        found_user = User.find_by_username("Cindy")   
        self.assertEqual(found_user.password,test_user.password)

class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the credentials class behaviours.
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credentials=Credentials("Gmail","CindyNyambu","gitz254")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credentials.account,"Gmail")
        self.assertEqual(self.new_credentials.name,"CindyNyambu")
        self.assertEqual(self.new_credentials.password,"gitz254")

    def test_save_credentials(self):
        '''
        test case to test if the credentrials object is saved into the credentials list.
        '''
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)        






if __name__ == '__main__':
    unittest.main()

    