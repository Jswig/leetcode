# Anders Poirel

# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums_0 = nums[0]
        start_idx = 0
        end_idx = len(nums)-1
        
        while start_idx < end_idx:
            print(f"start: {start_idx}, end: {end_idx}")
            new_idx = (start_idx + end_idx) // 2 
            if nums[new_idx] < nums_0:
                end_idx = new_idx
            else:
                start_idx = new_idx + 1
                
        return min(nums_0, nums[end_idx])