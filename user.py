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

           
