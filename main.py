import json
import os


class person():
    def __init__(self, fname, lname, age, sex, location, occupation):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.sex = sex
        self.location = location
        self.job = occupation


def getUserData():
    # Gather user data
    fname = input("Dream: What is Your First Name? \nUser:")
    lname = input("Dream: What is your Last Name? \nUser: ")
    age = input("Dream: What is your age? \n{} {}: ".format(fname, lname))
    sex = input("Dream: What is your Gender? \n{} {}: ".format(fname, lname))
    location = input(
        "Dream: Where Do you Live? \n{} {}: ".format(fname, lname))
    occupation = input(
        "Dream: What Do You Do For a Living? \n{} {}: ".format(fname, lname))

    user = person(fname, lname, age, sex, location, occupation)

    print(user.fname)


if not os.path.exists('data/personal.json'):
    # Path Does Not Exist
    # print("Path Does Not Exist")
    getUserData()

    exit()
with open('data/personal.json', 'r') as personal_data:
    # Open For Reading
    print("Open For Reading")
