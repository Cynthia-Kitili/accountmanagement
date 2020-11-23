import pyperclip
import random
import string

# class User:
#     """
#     Class that generates new instances of Users.
#     """
#     user_list= []
#     def __init__(self, username, password):
#         '''
#         Method that helps us define properties for our objects.
        
#         Args:
#             username: New User username.
#             password: New User password.
    
#         '''
#         self.username = username
#         self.password = password

#     def save_user(self):
#         '''
#         save_user method saves user objects into user_list.
#         '''
#         User.user_list.append(self) 

#     def delete_user(self):
#         '''
#         delete_user method deletes a saved user from the user_list.
#         '''
#         User.user_list.remove (self)    

#     @classmethod
#     def find_by_username(cls,username):
#         '''
#         Method that takes in a username and returns a user that matches that username.
#         '''
#         for user in cls.user_list:
#             if user.username == username:
#                 return user  

#     def display_user(cls):
#         '''
#         method that returns the user list
#         '''
#         return cls.user_list    

#     def user_exist(cls,username):
#         '''
#         Method that checks if a user exists from the user list.
#         '''
#         for user in cls.user_list:
#             if user.username == username:
#                     return True

#         return False  

#     def copy_password(cls,username):
#         user_found = User.find_by_username(username)
#         pyperclip.copy(user_found.password)

#     def verify_user(cls,username, password):
#         """
#         method to verify whether the user is in our user_list or not
#         """
#         a_user = ""
#         for user in User.user_list:
#             if(user.username == username and user.password == password):
#                     a_user == user.username
#         return a_user
        
#     def generatePassword(stringLength=8):
#         """
#         Generate a random password string of letters and digits and special characters
#         """
#         password = string.ascii_uppercase + string.ascii_lowercase + string.digits + "~!@#$%^&*"
#         return ''.join(random.choice(password) for i in range(stringLength))        
                   

           
class User:
    """
    Create User class that generates new instances of a user.
    """
    user_list = []

    def __init__(self, username, password):
        """
        method that defines the properties of a user.
        """
        self.username = username
        self.password = password

    def save_user(self):
        """
        A method that saves a new user instace into the user list
        """
        User.user_list.append(self)
    

    @classmethod
    def display_user(cls):
        return cls.user_list

    def delete_user(self):
        '''
        delete_account method deletes a  saved account from the list
        '''
        User.user_list.remove(self)