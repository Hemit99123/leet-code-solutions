class Solution:
    def makeFancyString(self, word: str) -> str:
        word = list(word)
        letter = word[0]
        counter = 0
        new_word = []

        for char in word:
            if char == letter:
                counter += 1
            else:
                letter = char
                counter = 1
            
            # Only add to new_word if counter is less than 3
            # because you must only add values that do not repeat 3 times consecutively
            if counter < 3:
                new_word.append(char)

        return "".join(new_word)
