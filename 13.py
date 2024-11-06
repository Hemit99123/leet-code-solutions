class Solution:
    def romanToInt(self, roman: str) -> int:
        numeral_reference = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        final_number = 0

        for i in range(len(roman)):
            # Get the current numeral's value
            arabic_number = numeral_reference[roman[i]]

            # Check if this numeral is smaller than the next one (subtraction case)
            if i + 1 < len(roman) and arabic_number < numeral_reference[roman[i + 1]]:
                final_number -= arabic_number
            else:
                final_number += arabic_number

        return final_number

