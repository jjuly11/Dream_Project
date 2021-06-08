#!/bin/env python3
import json
import os
# from nltk.tokenize import word_tokenize
# from nltk.stem import PorterStemmer

# Idea for later: encrypting and pickling the data out
# Idea for later: prompt for nickname or username

# Dictionary containing user information
user = {}

# The Project Information
name = 'Dream Project'
dev = "JJuly"
version = 1.0

# All intents 

question_intents = ["who","what","wht","qhat","ehat","shat","where","qhere","ehere","shere","wher","there","how","when","?", "wat","wen"]
user_personal_intents=["my","me","i","mine","am","user","use"]
non_personal_intents=["you","your","them","it"]
# Intents for the naming section
# This is used to try diffenect ways of saying the same thing even with diffenent spellings.
name_intents = ["name","bame","vame","hame","title","yitle","ritle","call","vall","xall"]
age_intents = ["age","years","year","old","aged","living"]
sex_intents = ["gender","sex","sexual","orientation"]
location_intents = ["location","residence","live","place","stay","staying"]


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
# ps = PorterStemmer()
user_query = ""
print(name+"\nVersion: " + str(version))

user_age_responces = ["You are {} years old".format(data["age"]),"Your age is {}".format(data['age'])]
user_location_responces = ["You are {} years old".format(data["age"]),"Your age is {}".format(data['age'])]
user_name_responces = ["Your name is {} {}".format(data["fname"],data["lname"]),"Is tis a trick question, you know I know you are {} {}".format(data["fname"],data["lname"])]
user_sex_responses = ["Your gender is {}".format(data['sex']),"Your sex is {}".format(data['sex'])]

while(not(user_query == "end" or user_query == "exit" or user_query == "good-bye")):
    # print("Enter this Loop")

    user_query = input("Dream: Ask me something else \n{} {}: ".format(
        data['fname'], data['lname']))
    # normalize text
    user_query = user_query.lower()
    # print(user_query)
    # print(user_query == "end")

    new_string = user_query.split(' ')
    # new_string = word_tokenize(user_query)

    for char in new_string:
        # word = ps.stem(char)
        print(char)
        for question in question_intents:
            if char == question:
                print(question)
                for word1 in new_string:
                    #sprint(word1)
                    for user_specific in user_personal_intents:
                        # print(user_specific)
                        if word1 == user_specific:
                            #print(word1==user_specific)
                            for word2 in new_string:
                                #print(word2)
                                for name_intent in name_intents:
                                    if word2 == name_intent:
                                        # print("in second if")
                                        #print("Dream: {} ".format(user_name_responces[0]))
                                        print(user_name_responces[0])
                                        break
                                if word2 == "age" or word2 == "old":
                                    # print("in second if")
                                    # print("Dream: Your Age is {}.".format(
                                        # data['age']))
                                    print(user_age_responces[0])
                                    breaks
                                # if user_query == "how are you?":
                                #     print("I am Fine, What about you?")
                                #     break
                    #The user_non_specific variable refers to things the user would ask the chatbot about itself 
                    for user_non_specific in non_personal_intents:
                    #Each word is compared to the one i the non_specific list to see if it matches both mispelling and possibilities.  
                        if word1 ==user_non_specific:
                            for word2 in new_string:
                                if word2 == "name" or word2 == "title":
                                    print("My name is the Project Dream but you could call me Dream for short.")
                                    
                                if word2 == "creator" or word2 == "maker":
                                    print("something")
                                if word2=="age" or word2=="years" or word2== "old":
                                    print("I am 1 week old or version {}".format(version))
                            # break
