#problem url https://leetcode.com/problems/backspace-string-compare/
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        p1 = self.helper(S, [])
        p2 = self.helper(T, [])
        return p1==p2
        
    def helper(self, S, stack):
        for char in S:
            if char != '#':
                stack.append(char)
            else:
                if not stack:
                    continue
                    
                stack.pop()
                
        return stack