# 1. Name:
#      Tristan Zatylny
# 2. Assignment Name:
#      Lab 06: Image Compression
# 3. Assignment Description:
#      This program will be given a json file that defines a grid's rows, columns, and the data in that grid.
#      The data in the grid can either be on or off. The data is represented by an array of numbers that
#      communicates how many runs of cells in a column in the grid are on or off. After a number of cells is
#      defined, the next number in that array is the opposite of what those cells just were. The program will
#      convert the json grid definition into a matrix. The matrix will either contain a true or false depending
#      on whether the cell is on or off. This will be done by using the json data's numbers to loop through the
#      matrix. After that is done, we will loop through the matrix, printing a hashtag whenever the value in the
#      cell is true or a space whenever the value in the cell is false.
# 4. Algorithmic Efficiency
#      The algroithmic efficiency of this code is O(n*m), where n is the number of input rows and m is the number
#      of input columns. The code has nested loops that run until they reach the maximum number of rows and columns.
# 5. What was the hardest part? Be as specific as possible.
#      The most difficult part of the assignment was figuring out how to create the grid. I initially tried syntax
#      similar to Java (grid = [max_rows][max_cols]) but then found out that that was wrong. After looking
#      up how to make a 2d array in Python, I was able to correct that mistake. Having the pseudocode as a reference
#      made the programming very simple.
# 6. How long did it take for you to complete the assignment?
#      1.5 hours

# Import json for file handling.
import json

# Get user input for the image file.
json_file = input("Please select a filename: ")

# Newline for console readability
print()

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
        max_rows = data_dictionary["num_rows"]
        max_cols = data_dictionary["num_columns"]
        data = data_dictionary["data"]

        # Set flag so code continues
        correct_format = True
    
    # JSON arguments aren't as expected
    except Exception as e:
        print(f"File has unexpected format: {e} not found.")
    
    # Ensure json file is in the expected format before continuing
    if correct_format:

        # Create a matrix for the image itself
        grid = [[False for x in range(max_cols)] for y in range(max_rows)] 


        # Loop through the data matrix and parse it.
        for col in range(max_cols):

            # Save the current matrix row as a list
            data_nums = data[col]

            # Define current row for iterating
            row = 0

            # Define variable to see what state the grid is in
            state = True

            # Loop through the numbers in the new list
            for number in data_nums:

                # Loop until each number's run has been satisfied
                for i in range(number):
                    
                    # Set current place in grid to the state according to the number
                    grid[row][col] = state

                    # Increment the row
                    row += 1
                
                # Flip the state for the next number
                state = not state

        # Loop through the grid for character printing
        for r in range(max_rows):
            for c in range(max_cols):

                # Print a # if the data is true
                if grid[r][c]:

                    # Print a character without a new line
                    print('#', end='')
                
                # Print a space if the data is false
                else:
                    
                    # Print a character without a new line
                    print(' ', end='')
            
            # Print a new line after each row loop
            print()
