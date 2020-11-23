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

    def credentials_exist(cls,number):
        '''
        Method that checks if a credntilas exists from the credentials list.
        '''
        for credentials in cls.credentials_list:
            if credentials.account == account:
                    return True

        return False

