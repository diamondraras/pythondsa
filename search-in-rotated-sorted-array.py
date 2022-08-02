"""
Problem statement https://leetcode.com/problems/search-in-rotated-sorted-array/
"""

class Solution:
    def binary_search(self,lo, hi, condition, default=0):
        while lo <= hi:
            mid = (lo + hi) // 2

            result = condition(mid, hi, lo)
            if result == 'found':
                return mid
            elif result == 'left':
                hi = mid - 1
            else:
                lo = mid + 1
        return default

    def search(self, nums: List[int], target: int) -> int:
        def count_rotation_condition(mid, hi, lo):
            
            if nums[mid-1]>nums[mid]:
                return "found"
            elif nums[mid] < nums[hi]:
                return "left"
            else :
                return "right"
        # count how many rotations has made
        rotations =  self.binary_search(0, len(nums)-1, count_rotation_condition)
        nums = nums[rotations:]+nums[:rotations]
        def normal_search_condition(mid, hi, lo):
            if nums[mid] == target:
                return "found"
            elif nums[mid] > target:
                return "left"
            else :
                return "right"
        # perform a standard binary search to find relative position
        position =  self.binary_search(0, len(nums)-1, normal_search_condition, default=-1)
        
        # calculate position based on rotated list
        if position == -1:
            resultat = -1
        elif rotations + position < len(nums):
            resultat = rotations + position
        else:
            resultat = rotations + position - len(nums)
        return resultat
