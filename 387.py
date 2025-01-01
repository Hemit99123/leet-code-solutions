def find_first_unique_character(input_string):
    # Dictionary to track occurrences
    char_dict = {}
    
    for char in input_string:
        if char in char_dict:
            # Remove the character if its occurrence exceeds 1
            del char_dict[char]
        else:
            # Add the character if not already present
            char_dict[char] = 1

    # Get the first remaining character in the dictionary
    for char in input_string:
        if char in char_dict:
            # Use index() to find its position in the string
            return input_string.index(char)

    # If no unique characters are found
    return -1

# Usage (using the function I made) 
input_string = input()
result = find_first_unique_character(input_string)
print("Index of the first unique character:", result)


