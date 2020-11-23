import pyperclip
import random
import string


class Credentials:
    '''
    Class that generates new instances of credentials.
    '''
    credentials_list = []
    
    def __init__(self,account,name,password):
        '''
        Method that helps us define properties for our objects.

        Args:
           account: New user account.
           name: New user name.
           password: New user password.
        '''

        self.account= account
        self.name=name
        self.password=password

    def save_credentials(self):
        '''
        saves credentials objects into credentials list.
        '''
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        '''
        Deletes a saved credential from the credentials list.
        '''
        Credentials.credentials_list.remove(self) 

    @classmethod
    def find_by_account(cls,account):
        '''
        Method that takes in an acount and returns credentials that matches that account.
        '''
        for credentials in cls.credentials_list:
            if credentials.account==account:
                return credentials    

    def display_credentials(cls):
        '''
        method that returns the credentials list
        '''
        return cls.credentials_list

    def credentials_exist(cls,account):
        '''
        Method that checks if a credntilas exists from the credentials list.
        '''
        for credentials in cls.credentials_list:
            if credentials.account == account:
                    return True

        return False

    def copy_password(cls,account):
        credentials_found = Credentials.find_by_account(account)
        pyperclip.copy(credentials_found.email)

    def verify_credentials(cls,account,name, password):
        """
        method to verify whether the credentials is in our credentials_list or not
        """
        a_credentials = ""
        for credentials in Credentials.credentials_list:
            if(credentials.account==account, credentials.name == name and credentials.password == password):
                    a_credentials == credentials.name
        return a_credentials

     def copy_password(cls,account):
        credentials_found = Credentials.find_by_account(account)
        pyperclip.copy(credentials_found.password)    
        
    def generatePassword(stringLength=8):
        """
        Generate a random password string of letters and digits and special characters
        """
        password = string.ascii_uppercase + string.ascii_lowercase + string.digits + "~!@#$%^&*"
        return ''.join(random.choice(password) for i in range(stringLength))    
 