import json
import os

# Idea for later: encrypting and pickling the data out

# Dictionary containing user information
user = {}

# The Project Information
name = 'Dream Project'
dev = "JJuly"
version = 1.0

# Class for user data (Pending usage).
# class person():
#     def __init__(self, fname, lname, age, sex, location, occupation):
#         self.fname = fname
#         self.lname = lname
#         self.age = age
#         self.sex = sex
#         self.location = location
#         self.job = occupation

# Function Collects user information and stores in dictionary(user).


def getUserData():
    '''
        This is a function that will prompt the user for thier personal information and store that information in the user dictionary defined at the beginning of the module.
    '''
    # Gather user data
    user['fname'] = input("Dream: What is Your First Name? \nUser:")
    user['lname'] = input("Dream: What is your Last Name? \nUser: ")
    user['age'] = input(
        "Dream: What is your age? \n{} {}: ".format(user['fname'], user['lname']))
    user['sex'] = input(
        "Dream: What is your Gender? \n{} {}: ".format(user['fname'], user['lname']))
    user['location'] = input(
        "Dream: Where Do you Live? \n{} {}: ".format(user['fname'], user['lname']))
    user['occupation'] = input(
        "Dream: What Do You Do For a Living? \n{} {}: ".format(user['fname'], user['lname']))

    # user = person(fname, lname, age, sex, location, occupation)

    # print(user.fname)

# This function takes the user information dictionary as an argument and stores it in a json file.


def write_json(user_data):
    '''
        This function takes the user information dictionary as an argument and stores it in a json file located in the data directory(personal.json).
    '''
    with open('data/personal.json', 'w') as output:
        json.dump(user_data, output, indent=2)


# If the file personal.json which is in the data directory exists then this initialization process is skipped.
if not os.path.exists('data/personal.json'):
    # Path Does Not Exist
    # print("Path Does Not Exist")
    getUserData()
    write_json(user)
    # Exits after initialized.
    exit()

# If user data is found in the file specified then the data is read a stored in a variable to be used in the module.

with open('data/personal.json', 'r') as personal_data:
    # Open For Reading
    data = json.load(personal_data)
    # print(data)
user_query = input("Dream: Hello, How's it going? \n{} {}: ".format(
    data['fname'], data['lname']))

while(not(user_query == "end" or user_query == "exit" or user_query == "good-bye")):
    # print("Enter this Loop")
    user_query = input("Dream: Oh that is intresting. \n{} {}: ".format(
        data['fname'], data['lname']))
    # print(user_query == "end")
