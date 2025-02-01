'''
4. Next Greater Element
Problem: For each element in an array, find the next greater element to the right. If there is no greater element, return -1.
Example:
Input: [4, 5, 2, 10, 8]
Output: [5, 10, 10, -1, -1]
''''


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if (nums1[i] == nums2[j]):
                    