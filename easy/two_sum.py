# Anders Poirel

# https://leetcode.com/problems/two-sum/

# Runtime: 48 ms, faster than 57.75% of Python3 online submissions for Two Sum.
# Memory Usage: 14.2 MB, less than 98.16% of Python3 online submissions for Two Sum.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        elems = dict()
        for i in range(len(nums)):
            if target-nums[i] in elems:
                return [i, elems[target-nums[i]]]
            elems[nums[i]] = i
        