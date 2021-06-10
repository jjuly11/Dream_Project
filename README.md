# Chatbot Psuedo Code (**Project Dream**)

This project is a simple chatbot for the user to conduct a conversation with. Althought simple this chatbot nicknamed Dream is robust and is able to handle multi meaning worlds and answer appropriately, If an answer isn't avaliable then it produces a random select message from its database stating that it doesn't understand the query. Dream Has a simple cli that allows the user to enter querys from 5 categories of which the question can be directed to the chatbot or asking the chatbot about the user themself.

##Feature List
+ Encrypts User Data
+ Is able to carry out a simple simple conversation based on 5 categories.
+ Very lightweight
+ Offers simple typo detection
+ Can recognize a small number of synonyms

## Initial Setup Stage (First Boot)

1. Produce initial setup, where **age**, **gender**, and **location**, **occupation**, **creator** is collected.
2. Save the information to a dictionary.
3. Generate encryption key and save in a safe place.
4. Encrypt the dictionary with the user's data.
5. Store encrypted information in json file for future use.


## Continuous Working (After Initial Setup)

1. Present the user with a start screen where they could either choose to re-enter there user data or continue as is. 
1. Start By Displaying the project name and version number as well as it's developer (JJ aka Joel July).
2. Check if a json file that contains the user's personal info is present.
3. If personal json file exsists and is not empty retreave information and proceed.
4. Else repeat initial setup process. 
5. Greet the user using their collected name.
6. Enter Loop while phrase is not good-bye or exit or end.
7. Prompt for user their query and save that to a variable.("User's Name: ")
8. Parse the user's query normalizing the text.(Make all words lowercase, reduce all words to their base)
9. Save all words into an list.
10. Remove all duplicate words using `set`.
11. Parse the array using `for` checking wach word against a precompiled list of intents.
12. If a match is met it the calls a function to choose a random respons from a predifined list of responses.
13. Else the next word in the array is tested.
14. If no result is found after the final word in the array tested then the genetric error messages is displayed.

