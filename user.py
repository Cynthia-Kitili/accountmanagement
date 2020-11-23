class User:
    """
    Class that generates new instances of Users.
    """
    user_list= []
    def __init__(self, username, password):
        '''
        Method that helps us define properties for our objects.
        
        Args:
            username: New User username.
            password: New User password.
    
        '''
        self.username = username
        self.password = password

    def save_user(self):
        '''
        save_user method saves user objects into user_list.
        '''
        User.user_list.append(self) 

    def delete_user(self):
        '''
        delete_user method deletes a saved user from the user_list.
        '''
        User.user_list.remove (self)    

    @classmethod
    def find_by_username(cls,username):
        '''
        Method that takes in a username and returns a user that matches that username.
        '''
        for user in cls.user_list:
            if user.username == username:
                return user  

    def display_user(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list    

    def user_exist(cls,number):
        '''
        Method that checks if a user exists from the user list.
        '''
        for user in cls.user_list:
            if user.username == username:
                    return True

        return False                 

           
