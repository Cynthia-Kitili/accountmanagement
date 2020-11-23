#!/usr/bin/env python3.9
from user import user
from credentials import Credentials

def create_new_user(username,password):
    '''
    Function to create a new user with a username and password
    '''
    new_user = User(username,password)
    return new_user

def save_user(user):
    '''
    Function to save a new user
    '''
    user.save_user()  

def display_user():
    """
    Function to display existing user
    """
    return User.display_user()      

def login_user(username,password):
    """
    function that checks whether a user exist and then login the user in.
    """
  
    confirm_user = Credentials.verify_user(username,password)
    return confirm_user  

def create_new_credentials(account,userName,password):
    """
    Function that creates new credentials for a given user account
    """
    new_credentials = Credentials(account,userName,password)
    return new_credentials   

def save_credentials(credentials):
    """
    Function to save Credentials to the credentials list
    """
    credentials. save_details()       