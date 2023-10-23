# Importing the pandas library
import pandas as pd

# Reading the csv file containing the NATO phonetic alphabet and storing it in a dataframe
df = pd.read_csv("nato_phonetic_alphabet.csv")

# Creating a dictionary where the keys are the letters and the values are the corresponding NATO phonetic codes
phino_dict = {row.letter: row.code for index, row in df.iterrows()}

# Printing the created dictionary
# print(phino_dict)

# Initializing a flag to control the user input loop
user_input_is_string = True

# Loop to prompt the user for input and handle exceptions
while user_input_is_string:
    # Asking the user to enter their name
    user_input = input("Enter your name: ")
    try:
        # Converting the user's name to uppercase and mapping each letter to its NATO phonetic code using the created
        # dictionary
        user_name_list = [phino_dict[i] for i in user_input.upper()]
    except KeyError:
        # Handling the case where an invalid input is provided
        print("Sorry, please enter a correct name.")
    else:
        # Setting the flag to exit the loop when valid input is provided
        user_input_is_string = False

# Printing the list of NATO phonetic codes corresponding to the user's name
print(user_name_list)
