# 1. Name:
#      Tristan Zatylny
# 2. Assignment Name:
#      Lab 02: Authentication
# 3. Assignment Description:
#      This program will read a JSON file called Lab02.json, parse the usernaes and passwords,
#      then prompt the user to 'log in' using one of those usernames and passwords
# 4. What was the hardest part? Be as specific as possible.
#      The most difficult part was finding out how the json library works. It was simple to look up, however.
#      After that, the most difficult part was finding out how to make a list out of a dictionary. Google's AI
#      summary was able to provide me with the correct answer. The rest of the program was simple.
# 5. How long did it take for you to complete the assignment?
#      1.5 hours

# Import json module for handling the file
import json

# Define variables we will need - lists for usernames and passwords, a string for the json file, and a temporary dictionary before the lists are filled
usernames = []
passwords = []
json_string = ""
temp_dict = {}

# Also define a flag variable so we continue only if the file is working and a variable with the file name
file_exists = False
json_file = "Lab02.json"

# Use a try-except to make sure the file exists.
try:
    # Open file and save it as a string
    with open(json_file) as f:
        json_string = f.read()
    
    # Set flag so code continues
    file_exists = True

# Catch to make sure the file exists
except FileNotFoundError:
    print(f"Unable to open file {json_file}.")

# Statement to ensure the file exists before running any other code
if file_exists:
    # Store the json in a temporary dictionary before it is lists
    temp_dict = json.loads(json_string)

    # Store dictionary items into respective lists
    usernames = temp_dict["username"]
    passwords = temp_dict["password"]

    # See if we're going through user input or test cases
    input_or_test = input("Go through user input instead of test cases (y/n)? ").lower()

    # While loop for test cases and counter to see which test case we should do
    done = False
    test_case = 1
    while not done:
        # User prompting
        if input_or_test == 'y':
            username = input("Username: ")
            password = input("Password: ")
            done = True # Only go through the program once for user input

        # Test cases
        else:
            # Match-case to go through test cases
            match test_case:
                case 1:
                    username = "John Cheese"
                    password = "None shall pass"
                case 2:
                    username = "Black Knight"
                    password = "Tis but a scratch."
                case 3:
                    username = "John Cheese"
                    password = "Tis but a scratch."
                case 4:
                    username = "King Arthur"
                    password = "Bring out your dead!"
                case 5:
                    username = "Black Knight"
                    password = "None shall pass"
                case 6:
                    username = "King Arthur"
                    password = "Run away!"
                case 7:
                    username = "French Soldier"
                    password = "I fart in your general direction"
                    # Last case, so set done to True
                    done = True
                # If we reach default case, something went wrong
                case _:
                    print("Case error - reached default case.")
                    quit() # Quit before something actually breaks
            print(f"\nTest case {test_case}: {username}, {password}")    


        # Variable to change if user was authenticated
        authenticated = False
        # Loop through usernames
        for i in range(len(usernames)):
            # See if user's username exists
            if username == usernames[i]:
                # Username does exist, check password
                if password == passwords[i]:
                    # Success
                    print("You are authenticated!")
                    authenticated = True
                # Incorrect password, break out of the loop
                else:
                    break

        # Either username doesn't exist or password was incorrect.
        if not authenticated:
            print("You are not authorized to use the system.")
        
        # Increment test case
        test_case = test_case + 1
