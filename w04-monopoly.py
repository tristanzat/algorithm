# 1. Name:
#      Tristan Zatylny
# 2. Assignment Name:
#      Lab 04: Monopoly
# 3. Assignment Description:
#      This program will determine if a hotel is able to be placed on Pennsylvania Avenue by asking a series of questions.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part of this was finding out which if statements needed to come first in order
#      to ensure that no unnecessary questions were asked and that the execution was efficient.
#      Once I figured that out, it was simple to program
# 5. How long did it take for you to complete the assignment?
#      1.5 hours

# Define variables for test cases
done = False
test_case = 1
expected_result = ""

# See if user is doing test cases and assign to boolean
testing = input("Run test cases? (y/n) ").lower() == 'y'

# Loop for test cases
while not done:

    # Don't loop if user is going through
    if not testing:
        done = True
    
    # Match-case to assign test case variables
    match test_case:
        case 1:
            expected_result = "Fail - Does not own enough"
            green_owned = 'n'
            pennsylvania_houses = 0
            pacific_houses = 0
            north_carolina_houses = 0
            num_hotels = 10
            num_houses = 10
            cash = 1000

        case 2:
            expected_result = "Fail - Poor"
            green_owned = 'y'
            pennsylvania_houses = 0
            pacific_houses = 0
            north_carolina_houses = 0
            num_hotels = 10
            num_houses = 15
            cash = 100

        case 3:
            expected_result = "Fail - No houses"
            green_owned = 'y'
            pennsylvania_houses = 0
            pacific_houses = 0
            north_carolina_houses = 0
            num_hotels = 10
            num_houses = 10
            cash = 9000

        case 4:
            expected_result = "Success - Swap with Pacific"
            green_owned = 'y'
            pennsylvania_houses = 4
            pacific_houses = 5
            north_carolina_houses = 4
            num_hotels = 0
            num_houses = 0
            cash = 0

        case 5:
            expected_result = "Success - Swap with NC"
            green_owned = 'y'
            pennsylvania_houses = 4
            pacific_houses = 4
            north_carolina_houses = 5
            num_hotels = 0
            num_houses = 0
            cash = 0

        case 6:
            expected_result = "Fail - Already built"
            green_owned = 'y'
            pennsylvania_houses = 5
            pacific_houses = 4
            north_carolina_houses = 4
            num_hotels = 10
            num_houses = 10
            cash = 1000

        case 7:
            expected_result = "Success - all at once"
            green_owned = 'y'
            pennsylvania_houses = 0
            pacific_houses = 0
            north_carolina_houses = 0
            num_hotels = 3
            num_houses = 12
            cash = 3000

        case 8:
            expected_result = "Success - house and hotel"
            green_owned = 'y'
            pennsylvania_houses = 3
            pacific_houses = 3
            north_carolina_houses = 3
            num_hotels = 1
            num_houses = 3
            cash = 5000
            done = True

        case _:
            done = True
    
    # Print which case is running for readability
    if testing:
        print(f"Case {test_case}: {expected_result}")

    # Prompt user  if not running test cases
    if not testing:
        # Prompt 1: Owning all green properties
        green_owned = input("Do you own all the green properties? (y/n) ").lower()

    # See if user owns all green properties
    if green_owned == 'y':

        # Prompt user if not running test cases
        if not testing:
            # Prompt 2: How many houses on Pennsylvania?
            pennsylvania_houses = int(input("What is on Pennsylvania Avenue? (0:nothing, 1:one house, ... 5:a hotel) "))

        # If Pennsylvania already has a hotel, no need to continue
        if pennsylvania_houses == 5:
            print("You cannot purchase a hotel if the property already has one.")

        # Pennsylvania doesn't have a hotel, continue
        else:
            
            # Prompt user if not running test cases
            if not testing:
                # Prompts 3 & 4: How many houses on each PA and NC?
                pacific_houses = int(input("What is on Pacific Avenue? (0:nothing, 1:one house, ... 5:a hotel) "))
                north_carolina_houses = int(input("What is on North Carolina Avenue? (0:nothing, 1:one house, ... 5:a hotel) "))

            # If there is already a hotel, swap it
            if pacific_houses == 5:
                print(f"Swap Pacific's hotel with Pennsylvania's {pennsylvania_houses} houses.")
            elif north_carolina_houses == 5:
                print(f"Swap North Carolina's hotel with Pennsylvania's {pennsylvania_houses} houses.")

            # No hotel for swapping, continue
            else:

                # Prompt user if not running test cases
                if not testing:
                    # Prompt 5: How many hotels are up for purchase?
                    num_hotels = int(input("How many hotels are there to purchase? "))

                # No hotels up for purchase
                if num_hotels == 0:
                    print("There are not enough hotels available for purchase at this time.")
                
                # At least one hotel is up for purchase, continue
                else:
                    
                    # Prompt user if not running test cases
                    if not testing:
                        # Prompt 6: How many houses are up for purchase?
                        num_houses = int(input("How many houses are there to purchase? "))

                    # See how many houses would be needed (12 maximum)
                    needed_houses = 12 - pennsylvania_houses - pacific_houses - north_carolina_houses

                    # See if there are enough houses to purchase
                    if num_houses >= needed_houses:
                        
                        # Prompt user if not running test cases
                        if not testing:
                            # Prompt 7: How much cash is there to spend?
                            cash = int(input("How much cash do you have to spend? $"))

                        # See how much cash is needed ($200 per house & hotel)
                        needed_cash = 200 * (needed_houses + 1)

                        # See if there is enough cash
                        if cash >= needed_cash:
                            
                            # Output transaction information
                            print(f"This will cost ${needed_cash}.\n" +
                            f"\tPurchase 1 hotel and {needed_houses} house(s).\n" +
                            f"\tPut 1 hotel on Pennsylvania and return any houses to the bank.")

                            # See if NC will need houses
                            if north_carolina_houses < 4:
                                print(f"\tPut {4-north_carolina_houses} house(s) on North Carolina.")
                            
                            # See if Pacific will need houses
                            if pacific_houses < 4:
                                print(f"\tPut {4-pacific_houses} house(s) on Pacific.")
                            
                        # Too poor
                        else:
                            print("You do not have sufficient funds to purchase a hotel at this time.")
                    
                    # Not enough houses
                    else:
                        print("There are not enough houses available for purchase at this time.")

    # User doesn't own all properties
    else:
        print("You cannot purchase a hotel until you own\n\tall the properties of a given color group.")
    
    # Run for unit tests
    if testing:
        
        # Move to the next test case
        test_case += 1
        
        # Newline for readability
        print()