# Anders Poirel

# https://leetcode.com/problems/search-in-rotated-sorted-array/
# Runtime: 36 ms, faster than 89.72% of Python3 online submissions for Search in Rotated Sorted Array.
# Memory Usage: 14.8 MB, less than 21.72% of Python3 online submissions for Search in Rotated Sorted Array.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target == nums[0]:
            return 0
        
        start_idx = 0
        end_idx = len(nums) - 1
        
        if target >= nums[0]:
            while True:
                new_idx = (start_idx + end_idx) // 2
                print(f"start: {start_idx}, end: {end_idx}\n")
                if nums[new_idx] == target:
                    return new_idx
                elif start_idx == end_idx:
                    break
                elif (nums[new_idx] > target) or (nums[new_idx] < nums[0]):
                    end_idx = new_idx
                else:
                    start_idx = new_idx + 1

                    
        else: # target < nums[0]
            while True:
                new_idx = (start_idx + end_idx) // 2
                print(f"start: {start_idx}, end: {end_idx}\n")
                if nums[new_idx] == target:
                    return new_idx 
                elif start_idx == end_idx:
                    break
                elif (nums[new_idx] < target) or (nums[new_idx] > nums[-1]):
                    start_idx = new_idx + 1
                else:
                    end_idx = new_idx

        return -1