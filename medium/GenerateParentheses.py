# Anders Poirel
# 12-03-2020
#
# https://leetcode.com/problems/generate-parentheses/
# 
# Runtime: 28 ms, faster than 89.93% of Python3 online submissions for Generate Parentheses.
# Memory Usage: 13.2 MB, less than 91.11% of Python3 online submissions for Generate Parentheses.

class Solution:
    def build_sol(self, nleft, nright, curr, sols, n):
        print(curr)
        if nright > nleft or nleft > n:
            return
        elif len(curr) == n*2 - 2:
            sols.append("(" + curr + ")")
            print("(" + curr + ")")
        else:
            print("Recursive call")
            self.build_sol(nleft, nright+1, curr + ")", sols, n)
            self.build_sol(nleft+1, nright, curr + "(", sols, n)
        
    def generateParenthesis(self, n: int) -> List[str]:
        sols = []
        self.build_sol(1, 1, ")", sols, n)
        self.build_sol(2, 0, "(", sols, n)
        return sols
        
        