class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_vol = 0
        i = 0
        j = len(height)-1
        while i != j:
            vol = (j-i) * min(height[i], height[j])
            max_vol = vol if vol > max_vol else max_vol
            if height[j] < height[i]:
                j -= 1
            else:
                i += 1
        return max_vol
            
        
        