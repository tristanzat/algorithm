# 1. Name:
#      Tristan Zatylny
# 2. Assignment Name:
#      Lab 08: Sort
# 3. Assignment Description:
#      This program takes in a file, extracts an array, then performs selection sort on it.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was finding out where to put asserts since I usually handle that sort of
#      thing with try-except statements.
# 5. How long did it take for you to complete the assignment?
#      1 hour

# Import json for file handling.
import json

def start():
    testing = input("Do test cases (y/n)?").lower()

    if testing == "y":
        done = False
        test = 1

        while not done:
            file_input = test_case(test)
            __main__(file_input)
            print()
            

    else:
        file_input = user_input()
        __main__(file_input)
    


def __main__(json_file):
    
    # Flag to see if the file has been found
    file_exists = False

    # Use a try-except to make sure the file exists.
    try:
        # Open file and save it as a string
        with open(json_file) as f:
            json_string = f.read()
        
        # Assert string has content
        assert(json_string is not None)

        # Set flag so code continues
        file_exists = True

    # Catch to make sure the file exists
    except FileNotFoundError:
        print(f"Unable to open file {json_file}.")

    # Ensure the file exists before continuing
    if file_exists:
        
        # Store the json string as a dictionary
        data_dictionary = json.loads(json_string)

        # Flag to see if the file format is what is expected
        correct_format = False

        # Use a try-except to see if the file format follows what is expected
        try:
            
            # Parse dictionary into separate variables
            array = data_dictionary["array"]

            # Set flag so code continues
            correct_format = True
        
        # JSON arguments aren't as expected
        except Exception as e:
            print(f"File has unexpected format: {e} not found.")
        
        # Ensure json file is in the expected format before continuing
        if correct_format:
            
            # Sort the array
            array = sort_array(array)
            
            # Display the array
            print(f"The values in {json_file} are:")
            display_array(array)

def user_input():
    # Get user input for the image file.
    user_input = input("What is the name of the file? ")

    # Fix file name to match my file structure
    user_input = "w08/" + user_input

    return user_input

def test_case(case_number):
    match (case_number):
        case 1:
            return "w08/Lab08.empty.json"
        case 2:
            return "w08/Lab08.trivial.json"
        case 3:
            return "w08/Lab08.languages.json"
        case 4:
            return "w08/Lab08.states.json"
        case 5:
            return "w08/Lab08.cities.json"
        case default:
            assert(False)
            return ""

def sort_array(array):

    # Assert array is a list
    assert isinstance(array, list)
    
    # Array needs more than 1 element to be sorted
    if len(array) <= 1:
        return array

    else:
        # Start looping for the sort
        for sort_index in range(len(array)-1, 0, -1):
            
            # Assume largest index is first
            largest_index = 0

            for i in range(1, sort_index + 1):

                if array[i] > array[largest_index]:
                    largest_index = i
            
            array[sort_index], array[largest_index] = array[largest_index], array[sort_index]
    
    assert_sorted(array)

    return array

def display_array(array):
    
    # Assert array is a list
    assert isinstance(array, list)

    # Display items on new lines with a tab before each
    for item in array:
        print(f"\t{item}")

def assert_sorted(array):

    # Assert array is a list
    assert isinstance(array, list)

    # Sorted if array has one or zero items
    if len(array) <= 1:
        return True

    # Loop through and compare
    for i in range(1, len(array) - 1):
        assert(array[i-1] < array[i])
    
    return True
    
__main__()