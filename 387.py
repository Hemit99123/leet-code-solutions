class Solution:
    def firstUniqChar(self, s: str) -> int:

        # Dictionary to track occurrences
        char_dict = {}
        
        for char in s:
            if char in char_dict:
                # Remove the character if its occurrence exceeds 1
                del char_dict[char]
            else:
                # Add the character if not already present
                char_dict[char] = 1

        # Get the first remaining character in the dictionary
        for char in s:
            if char in char_dict:
                # Use index() to find its position in the string
                return s.index(char)

        # If no unique characters are found
        return -1
