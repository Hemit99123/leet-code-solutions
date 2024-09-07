class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        h = {}

        for item in nums:
            if item in h:
                h[item] += 1
            else:
                h[item] = 1

        max_amount = n/2

        for key, value in h.items():
            if value > max_amount:
                return key
        
        return 0
