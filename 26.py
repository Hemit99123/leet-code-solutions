from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Pointer for the position of unique elements
        unique_index = 1
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[unique_index] = nums[i]
                unique_index += 1
        
        return unique_index  # The new length of the list with unique elements