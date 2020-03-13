# Anders Poirel
# 11-03-2020

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        elems = dict()
        for i in range(len(nums)):
            if target-nums[i] in elems:
                return [i, elems[target-nums[i]]]
            elems[nums[i]] = i
        