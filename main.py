#!/bin/env python3
import json
import os
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import random

# Idea for later: encrypting and pickling the data out
# Idea for later: prompt for nickname or username

# Dictionary containing user information
user = {}

# The Project Information
name = 'Dream Project'
dev = "JJuly"
version = 1.0

# If a response has been found
responded=False
# Ends the Entire Program or the While Loop
finalEnd=True

# All intents 
question_intents = ["who","what","wht","qhat","ehat","shat","where","qhere","ehere","shere","wher","there","how","when","?", "wat","wen"]
non_personal_intents=["you","your","them","it"]
user_personal_intents=["my","me","i","mine","am","user","use"]

# --User Intents
# Intents for the naming section
# This is used to try diffenect ways of saying the same thing even with diffenent spellings.
name_intents = ["name","bame","vame","hame","title","yitle","ritle","call","vall","xall","?","/"]
age_intents = ["age","years","year","old","aged","living","?","/"]
sex_intents = ["gender","sex","sexual","orientation","?","/"]
location_intents = ["location","residence","live","place","stay","staying","found","?","/"]
occupation_intents = ["do","do?","do/","d0","d0?","d0/","work","work?","work/","w0rk","w0rk?","w0rk/","occupation","0ccupation","function","function?","function/","functi0n?","functi0n/","?","/"]

# --ChatBot Intents
chatbot_name_intents=["name","bame","name?","name/","vame","hame","title","title?","title?","yitle","ritle","call","vall","xall","label","version","?","/"]
chatbot_age_intents=["age","age/","age?","years","years/","years?","year","year/","year?","year>","year\\","old","0ld","old?","old/","old\"","aged","aged?","aged/","living","living?","living/","?","/"]
chatbot_location_intents=["location","locati0n","locati0n?","locati0n/","location?","location/","residence","residence?","residence/","live","live?","live/","living","place","stay","staying","where","found","?","/"]
chatbot_sex_intents=["gender","sex","sexual","orientation","?","/"]
chatbot_dev_intents=["dev","devs","div","sev","fev","xev","developers","developer","maker","creator","father","mother","?","/"]
chatbot_occupation_intents=["do","do?","do/","d0","d0?","d0/","work","work?","work/","w0rk","w0rk?","w0rk/","occupation","0ccupation","function","function?","function/","functi0n?","functi0n/","job","j0b","?","/"]


# Greetings Intents 

greeting_intents = ["hello","hi","hola","howdy","hey","yo"]

# End intents

end_intents = ["end", "goodbye","bye","later","until","exit"]


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
ps = PorterStemmer()
user_query = ""
print(name+"\nVersion: " + str(version))

# Responses Lists
# --User
# Is used to when the user asks a question about themself.
# Generates a custom response based on the user personal data collected.
user_age_responses = ["Dream: You are {} years old".format(data["age"]),"Dream: Your age is {}".format(data['age'])]
user_location_responses = ["Dream: You Live nn/at {}.".format(data["location"])]
user_name_responses = ["Dream: Your name is {} {}".format(data["fname"],data["lname"]),"Dream: Is tis a trick question, you know I know you are {} {}".format(data["fname"],data["lname"])]
user_sex_responses = ["Dream: Your gender is {}".format(data['sex']),"Dream: Your sex is {}".format(data['sex'])]
user_occupation_responses = ["You are a {}".format(data["occupation"]),"You do {}".format(data["occupation"])]

# --Chatbot
chatbot_name_responses = ["Dream: My name is Project Dream or Dream For short"]
chatbot_location_responses = ["Dream: I live inside your computer.","Dream: I can be found on a componect inside your computer called ram or memory"]
chatbot_sex_responses = ["Dream: I Have no gender","I am am a computer program with no gender","Dream: I am any gender you choose"]
chatbot_age_responses = ["Dream: I am no more than a year old","Dream: I am immortal","I will live forever", "Dream: I have no age but i am versin {}".format(version)]
chatbot_dev_responses = ["Dream: I was created by {}".format(dev),"Dream: I was invisioned and brought to life by {}".format(dev),"Dream: It was {} Who Created me".format(dev)]
chatbot_occupation_responses = ["I am a program create to emulate a conversations","I am here to speak to you","My Job is to speak to you."]


# Greetings Responses

greeting_responses = ["Hello","Longtime no talk","Good to interact with you again","Good to see you","Hey!!!!","Who is this? lol ,just kidding :)"]

# End Responses

end_responses = ["Great Talk","GoodBye","Later","Bye","Until we meet again","Love You!","Take Care of yourself", "Remember to social distance","Stay Safe"]

# Don't Understand Responces

dont_undestand_responses = ["I don't understand", "What was that?", "Sorry I don't think i know how to answer that.","Please try again after I have been updated.","Try again, But simpler please","Please ask a easier question","Sorry I Don't Know","My Database Doesn't Contain the answer to that."]

while(finalEnd):
    # print("Enter this Loop")
    responded=False

    user_query = input("Dream: Ask me something else \n{} {}: ".format(
        data['fname'], data['lname']))
    # normalize text
    user_query = user_query.lower()
    
    # print(user_query)
    # print(user_query == "end")

    # new_string = user_query.split(' ')

    # Using the nltk tokenizer to conver the user input string into a list. 
    new_string = word_tokenize(user_query)

    for char in new_string:
        # Loops through the list of the user's input that was converted to list.
        # While at the same time the saves a element of the list to the variable char.
        # Uses the nltk stemmer to reduce each word to its root word
        word = ps.stem(char)
        # print(char)

        # Loops through the questions intents list
        for question in question_intents:
            # Checking each intent form the questions list to see if it matches the user input.
            # If it matches then it moves on else prints a error that says it does not understand.
            if char == question:
                
                # If it is a question then it loops through the user input a second time to find out if the user is asking about themself or the chatbot.
                for word1 in new_string:
                    
                    # The user input is once again compared against each element in a intents list.
                    for user_specific in user_personal_intents:
                        

                        # If the user is asking about themself then the responces are pulled from the personal file, added to the predefined responces list and displayed.
                        if word1 == user_specific:
                            
                            # Once again we loop through a third time but this time we are checking for the main intent the user wishes to convey. 
                            for word2 in new_string:
                                
                                # The Uses input is looped through again.
                                for name_intent in name_intents:

                                    # If the user mentioned anything about names or any synonyme of name then it will enter else it go onto the other check.
                                    if word2 == name_intent and responded==False:
                                        
                                        # If the user main intention is the name then a responce pertaining to the name is pulled from the name responses list.
                                        print(random.choice(user_name_responses))
                                        responded=True
                                        # After the answer is presented a break out of the loop occurs were the user is once again prompted for their input.
                                        break
                                
                                # At this point the process out lined above repeats with minimal changes.
                                for age_intent in age_intents:

                                    if word2 == age_intent and responded==False:
                                        print(random.choice(user_age_responses))
                                        responded=True
                                        break
                                for location_intent in location_intents:

                                    if word2 == location_intent and responded==False:
                                        print(random.choice(user_location_responses))
                                        responded=True
                                        break
                                for sex_intent in sex_intents:

                                    if word2 == sex_intent and responded==False:
                                        print(random.choice(user_sex_responses))
                                        responded=True
                                        break
                                for occupation_intent in occupation_intents:

                                    if word2 == occupation_intent and responded==False:
                                        print("Dream: "+random.choice(user_occupation_responses))
                                        responded=True
                                        break
                    #The user_non_specific variable refers to things the user would ask the chatbot about itself 
                    for user_non_specific in non_personal_intents:

                    #Each word is compared to the one i the non_specific list to see if it matches both mispelling and possibilities.  
                        if word1 ==user_non_specific:
                            for word2 in new_string:
                                for chatbot_name_intent in chatbot_name_intents:
                                    
                                    if word2 == chatbot_name_intent and responded==False:
                                        print(random.choice(chatbot_name_responses))
                                        responded=True
                                        break
                                for chatbot_age_intent in chatbot_age_intents:
                                    if word2 == chatbot_age_intent and responded==False:
                                        print(random.choice(chatbot_age_responses))
                                        responded=True
                                        break
                                for chatbot_sex_intent in chatbot_sex_intents:
                                    if word2 == chatbot_sex_intent and responded==False:
                                        print(random.choice(chatbot_sex_responses))
                                        responded=True
                                        break
                                for chatbot_location_intent in chatbot_location_intents:
                                    if word2 == chatbot_location_intent and responded==False:
                                        print(random.choice(chatbot_location_responses))
                                        responded=True
                                        break
                                for chatbot_dev_intent in chatbot_dev_intents:
                                    if word2 == chatbot_dev_intent and responded==False:
                                        print(random.choice(chatbot_dev_responses))
                                        responded=True
                                        break
                                for chatbot_occupation_intent in chatbot_occupation_intents:
                                    if word2 == chatbot_occupation_intent and responded==False:
                                        print("Dream: "+random.choice(chatbot_occupation_responses))
                                        responded=True
                                        break

                                # break
                                
            for greeting_intent in greeting_intents:
                # Handles the Greetings    
                if char == greeting_intent:
                    print("Dream: {}".format(random.choice(greeting_responses)))
                    responded=True
                    break
            for end_intent in end_intents:
                if char == end_intent:
                    # Handles the End greetings
                    print("Dream: {}".format(random.choice(end_responses)))
                    responded=True
                    finalEnd=False
                    break
            #breaks the loop if a response is found.
            if(responded):
                break
        # If the User input is not in the intents or database
        if(responded):
            # print("found response")
            break;
        else:
            print("Dream: {}".format(random.choice(dont_undestand_responses)))
            break