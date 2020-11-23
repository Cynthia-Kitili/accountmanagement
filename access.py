#!/usr/bin/env python3.9
from user import User
from credentials import Credentials

# def create_user(username,password):
#     '''
#     Function to create a new user 
#     '''
#     new_user = User(username,password)
#     return new_user

# def save_user(user):
#     '''
#     Function to save a new user
#     '''
#     user.save_user()  

# def display_user():
#     """
#     Function to display existing user
#     """
#     return User.display_user()      

# def login_user(username,password):
#     """
#     Function that checks whether a user exist and then login the user.
#     """
  
#     confirm_user = Credentials.verify_user(username,password)
#     return confirm_user  

# def create_credentials(account,userName,password):
#     """
#     Function that creates new credentials for a given user account
#     """
#     new_credentials = Credentials(account,userName,password)
#     return new_credentials   

# def save_credentials(credentials):
#     """
#     Function to save Credentials to the credentials list
#     """
#     credentials. save_details()   

# def display_account_details():
#     """
#     Function that returns all saved credentials.
#     """
#     return Credentials.display_credentials()  

# def find_credentials(account):
#     """
#     Function that finds a Credential by an account name and returns the Credentials that belong to that account
#     """
#     return Credentials.find__by_account(account)    

# def check_credendtials(account):
#     """
#     Function that checks if a Credentials exists with that account name and return true or false
#     """
#     return Credentials.if_credentials_exist(account)    

# def generate_Password():
#     '''
#     Function that generates a random password for the user.
#     '''
#     auto_password=Credentials.generatePassword()
#     return auto_password    

# def copy_password(account):
#     """
#     Function that copies the password using the pyperclip framework.
#     """
#     return Credentials.copy_password(account)    

# def delete_credentials(credentials):
#     """
#     Function that delete a Credentials from credentials list
#     """
#     credentials.delete_credentials()   

# def access():
#     print("Hello Welcome to your accounts access application. What is your name?")
#     your_name=input()

#     print(f"Hello {your_name}.What would you like to do?")
#     print('\n')

#     while True:
#         print("Use these short codes: ca- create account, ha- have account")

#         short_code = input().lower()
            
#         if short_code == "ca":
#             print("Sign up to create new account")
#             print("-"*100)
#             username = input ("Username:")
#             while True:
#                 print("Use these password short codes: gp-generate password, tp-type password ")
#                 password_short_code == input().lower().strip()
#                 if password_short_code == "tp":
#                     password = input ("Password:\n")
#                     break
#                 elif password_short_code == "gp":
#                     password= generate_Password()    
#                     break
#                 else:
#                     print("Invalid password, try again")    
#             save_user(create_user(username, password))   
#             print("-"*100)
#             print(f"Hello {username}, Your account has been created succesfully! Your password is : {password}")     
#             print("-"*100)
#         elif short_code == "ha":
#             print("-"*100)
#             print("Enter your Username and your Password to log in:")
#             print('-' * 100)
#             username = input("Username: ")
#             password = input("password: ")
#             login = login_user(username,password)
#             if login_user == login:
#                 print(f"Hello {username}.Welcome to your account")  
#                 print('\n')
#             while True:
#                 print("Use these short codes: cc- Create new Credential, dc- Display Credentials, gp- generate password d-Delete, e-Exit application  ")
#                 short_code= input().lower().strip()
#                 if short_code == "cc":
#                     print("Create New Credential")
#                     print("-"*50)
#                     print("Enter Account name :")
#                     account = input().lower()
#                     print("Enter Account username:")
#                     name = input()
#                     while True:
#                         print(" tp -Type pasword if you already have an account:\n gp -Generate Password")
#                         password_short_code = input().lower().strip()
#                         if password_short_code == 'tp':
#                             password = input("Enter Your Own Password:\n")
#                             break
#                         elif password_short_code == 'gp':
#                             password = generate_Password()
#                             break
#                         else:
#                             print("Invalid password, try again")
#                     save_credentials(create_credentials(account,name,password))
#                     print('\n')
#                     print(f"Account Credential for: {account} with Username: {name} and Password:{password} has been created succesfully!")
#                     print('\n')
#                 elif short_code == "dc":
#                     if display_account_details():
#                         print("Below is a list of your acoounts: ")
                 
#                         print('*' * 50)
#                         print('_'* 50)
#                         for account in display_account_details():
#                             print(f" Account:{account.account} \n Username:{username}\n Password:{password}")
#                             print('_'* 50)
#                             print('*' * 50)
#                     else:
#                         print("You don't have any credentials saved yet.")  
#                 elif short_code == "fc":
#                     print("Enter the Account Name you want to search for")
#                     search_name = input().lower()
#                     if find_credential(search_name):
#                         search_credentials = find_credentials(search_name)
#                         print(f"Account Name : {search_credentials.account}")
#                         print('-' * 50)
#                         print(f"User Name: {search_credentials.name} Password :{search_credentials.password}")
#                         print('-' * 50)
#                     else:
#                         print("That Credential does not exist")
#                         print('\n')   
#                 elif short_code == "d":
#                     print("Enter the Account name of the credentials you want to delete")
#                     search_name = input().lower()
#                     if find_credentials(search_name):
#                         search_credentials = find_credentials(search_name)
#                         print("_"*50)
#                         search_credentials.delete_credentials()
#                         print('\n')
#                         print(f"Your credentials for : {search_credentials.account} have been successfully deleted!!!")
#                         print('\n')
#                     else:
#                         print("That Credential you want to delete does not exist.")
#                 elif short_code == 'gp':
#                     password = generate_Password()
#                     print(f" {password} has been generated. ")
#                 elif short_code == 'ex':
#                     print("Thanks for using password manager application.")
#                     break
#                 else:
#                     print("Please enter a valid input to continue")

# if __name__ == '__main__':
#     access()        

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
  
    check_user = Credentials.verify_user(username,password)
    return check_user

def create_new_credential(account,userName,password):
    """
    Function that creates new credentials for a given user account
    """
    new_credential = Credentials(account,userName,password)
    return new_credential
def save_credentials(credentials):
    """
    Function to save Credentials to the credentials list
    """
    credentials. save_details()
def display_accounts_details():
    """
    Function that returns all the saved credential.
    """
    return Credentials.display_credentials()

def delete_credential(credentials):
    """
    Function to delete a Credentials from credentials list
    """
    credentials.delete_credentials()

def find_credential(account):
    """
    Function that finds a Credentials by an account name and returns the Credentials that belong to that account
    """
    return Credentials.find_credential(account)
def check_credendtials(account):
    """
    Function that check if a Credentials exists with that account name and return true or false
    """
    return Credentials.if_credential_exist(account)

def generate_Password():
    '''
    generates a random password for the user.
    '''
    auto_password=Credentials.generatePassword()
    return auto_password
def copy_password(account):
    """
    A funct that copies the password using the pyperclip framework
    We import the framework then declare a function that copies the emails.
    """
    return Credentials.copy_password(account)


def passlocker():
    print("Hello Welcome to your Accounts Password Store...\n Please enter one of the following to proceed.\n CA ---  Create New Account  \n LI ---  Have An Account  \n")
    short_code=input("").lower().strip()
    if short_code == "ca":
        print("Sign Up")
        print('*' * 50)
        username = input("User_name: ")
        while True:
            print(" TP - To type your own pasword:\n GP - To generate random Password")
            password_Choice = input().lower().strip()
            if password_Choice == 'tp':
                password = input("Enter Password\n")
                break
            elif password_Choice == 'gp':
                password = generate_Password()
                break
            else:
                print("Invalid password please try again")
        save_user(create_new_user(username,password))
        print("*"*85)
        print(f"Hello {username}, Your account has been created succesfully! Your password is: {password}")
        print("*"*85)
    elif short_code == "li":
        print("*"*50)
        print("Enter your User name and your Password to log in:")
        print('*' * 50)
        username = input("User name: ")
        password = input("password: ")
        login = login_user(username,password)
        if login_user == login:
            print(f"Hello {username}.Welcome To PassWord Locker Manager")  
            print('\n')
    while True:
        print("Use these short codes:\n CC - Create a new credential \n DC - Display Credentials \n FC - Find a credential \n GP - Generate A randomn password \n D - Delete credential \n EX - Exit the application \n")
        short_code = input().lower().strip()
        if short_code == "cc":
            print("Create New Credential")
            print("."*20)
            print("Account name ....")
            account = input().lower()
            print("Your Account username")
            userName = input()
            while True:
                print(" TP - To type your own pasword if you already have an account:\n GP - To generate random Password")
                password_Choice = input().lower().strip()
                if password_Choice == 'tp':
                    password = input("Enter Your Own Password\n")
                    break
                elif password_Choice == 'gp':
                    password = generate_Password()
                    break
                else:
                    print("Invalid password please try again")
            save_credentials(create_new_credential(account,userName,password))
            print('\n')
            print(f"Account Credential for: {account} - UserName: {userName} - Password:{password} created succesfully")
            print('\n')
        elif short_code == "dc":
            if display_accounts_details():
                print("Here's your list of acoounts: ")
                 
                print('*' * 30)
                print('_'* 30)
                for account in display_accounts_details():
                    print(f" Account:{account.account} \n User Name:{username}\n Password:{password}")
                    print('_'* 30)
                print('*' * 30)
            else:
                print("You don't have any credentials saved yet..........")
        elif short_code == "fc":
            print("Enter the Account Name you want to search for")
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print(f"Account Name : {search_credential.account}")
                print('-' * 50)
                print(f"User Name: {search_credential.userName} Password :{search_credential.password}")
                print('-' * 50)
            else:
                print("That Credential does not exist")
                print('\n')
        elif short_code == "d":
            print("Enter the account name of the Credentials you want to delete")
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print("_"*50)
                search_credential.delete_credentials()
                print('\n')
                print(f"Your stored credentials for : {search_credential.account} successfully deleted!!!")
                print('\n')
            else:
                print("That Credential you want to delete does not exist in your store yet")

        elif short_code == 'gp':

            password = generate_Password()
            print(f" {password} Has been generated succesfull. You can proceed to use it to your account")
        elif short_code == 'ex':
            print("Thanks for using passwords store manager.. See you next time!")
            break
        else:
            print("Wrong entry... Check your entry again and let it match those in the menu")
    else:
        print("Please enter a valid input to continue")

if __name__ == '__main__':
    passlocker()









