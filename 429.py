class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if (nums1[i] == nums2[j]):
                    