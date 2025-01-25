# Brute force method O(n^2)
# Ineffient solution:

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = []

        for index1 in range(len(temperatures)):
            days_passed = 1
            for index2 in range(index1 + 1, len(temperatures)):  # Only compare with subsequent days
                if temperatures[index2] > temperatures[index1]:  # Check if temperature increases
                    answer.append(days_passed)  # Record the number of days
                    break
                else:
                    days_passed += 1
            else:
                answer.append(0)  # If no warmer day is found, append 0

        return answer
