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

def __main__():
    # Get user input for the image file.
    json_file = input("What is the name of the file? ")

    # Fix file name to match my file structure
    json_file = "w08/" + json_file

    # Flag to see if the file has been found
    file_exists = False

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
            display_array(array)

def sort_array(array):
    
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
    
    return array

def display_array(array):
    
    # Display items on new lines with a tab before each
    for item in array:
        print(f"\t{item}")
    
__main__()