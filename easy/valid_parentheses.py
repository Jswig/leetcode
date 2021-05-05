# Anders Poirel

# https://leetcode.com/problems/valid-parentheses

# Runtime: 28 ms, faster than 71.23% of Python3 online submissions for Valid Parentheses.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Valid Parentheses.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for i in range(len(s)):
            if s[i] in ['{', '[', '(']:
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                res = stack.pop()
                if s[i] == '}' and res != '{':
                    return False
                elif s[i] == ']' and res != '[':
                    return False
                elif s[i] == ')' and res != '(':
                    return False 
                
        return True if len(stack) == 0 else False