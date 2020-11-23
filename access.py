#!/usr/bin/env python3.9
from user import user
from credentials import Credentials

def create_user(username,password):
    '''
    Function to create a new user 
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
    Function that checks whether a user exist and then login the user.
    """
  
    confirm_user = Credentials.verify_user(username,password)
    return confirm_user  

def create_credentials(account,userName,password):
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

def display_account_details():
    """
    Function that returns all saved credentials.
    """
    return Credentials.display_credentials()  

def find_credentials(account):
    """
    Function that finds a Credential by an account name and returns the Credentials that belong to that account
    """
    return Credentials.find__by_account(account)    

def check_credendtials(account):
    """
    Function that checks if a Credentials exists with that account name and return true or false
    """
    return Credentials.if_credentials_exist(account)    

def generate_Password():
    '''
    Function that generates a random password for the user.
    '''
    auto_password=Credentials.generatePassword()
    return auto_password    

def copy_password(account):
    """
    Function that copies the password using the pyperclip framework.
    """
    return Credentials.copy_password(account)    

def delete_credentials(credentials):
    """
    Function that delete a Credentials from credentials list
    """
    credentials.delete_credentials()   

def access():
    print("Hello Welcome to your accounts access application. What is your name?")
        your_name=input()

        print(f"Hello {your_name}.What would you like to do?")
        print('\n')

        while True:
            print("Use these short codes: ca- create account, ha- have account")

            short_code = input().lower()
            
            if short_code == "ca":
                print("Sign up to create new account")
                print("-"*100)
                username = input ("Username:")
                while True:
                    print("Use these password short codes: gp-generate password, tp-type password ")
                    password_short_code == input().lower().strip()
                    if password_short_code == "tp":
                        password = input ("Password:\n")
                        break
                    elif password_short_code == "gp":
                        password= generate_Password()    
                        break
                    else:
                        print("Invalid password, try again")    
                save_user(create_user(username, password))   
                print("-"*100)
                print(f"Hello {username}, Your account has been created succesfully! Your password is : {password}")     
                print("-"*100)
        elif short_code == "ha":
            print("-"*100)
            print("Enter your Username and your Password to log in:")
            print('-' * 100)
            username = input("Username: ")
            password = input("password: ")
            login = login_user(username,password)
            if login_user == login:
                print(f"Hello {username}.Welcome to your account")  
                print('\n')
        while True:
            print("Use these short codes: cc- Create new Credential, dc- Display Credentials, gp- generate password d-Delete, e-Exit application  ")
            short_code= input().lower().strip()
            if short_code == "cc":
                print("Create New Credential")
                print("-"*50)
                print("Enter Account name :")
                account = input().lower()
                print("Enter Account username:")
                name = input()
                while True:
                    print(" tp -Type pasword if you already have an account:\n gp -Generate Password")
                    password_short_code = input().lower().strip()
                    if password_short_code == 'tp':
                        password = input("Enter Your Own Password:\n")
                        break
                    elif password_short_code == 'gp':
                        password = generate_Password()
                        break
                    else:
                    print("Invalid password, try again")
                save_credentials(create_credentials(account,name,password))
                print('\n')
                print(f"Account Credential for: {account} with Username: {name} and Password:{password} has been created succesfully!")
                print('\n')
            elif short_code == "dc":
                if display_account_details():
                    print("Below is a list of your acoounts: ")
                 
                    print('*' * 50)
                    print('_'* 50)
                    for account in display_account_details():
                        print(f" Account:{account.account} \n Username:{username}\n Password:{password}")
                        print('_'* 50)
                    print('*' * 50)
                else:
                print("You don't have any credentials saved yet.")  
            elif short_code == "fc":
                print("Enter the Account Name you want to search for")
                search_name = input().lower()
                if find_credential(search_name):
                    search_credentials = find_credentials(search_name)
                    print(f"Account Name : {search_credentials.account}")
                    print('-' * 50)
                    print(f"User Name: {search_credentials.name} Password :{search_credentials.password}")
                    print('-' * 50)
                else:
                    print("That Credential does not exist")
                    print('\n')      










