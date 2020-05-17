#problem url https://leetcode.com/problems/first-unique-character-in-a-string/
from collections import OrderedDict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        od = OrderedDict()
        result = -1
        for i in range(len(s)):
            if s[i] not in od:
                od[s[i]] = (i, 1)
                
            else:
                od[s[i]] = (i, od[s[i]][1]+1)
                od.move_to_end(s[i])
        
        
        for i in od.values():
            if i[1] == 1:
                result = i[0]
                break
                
                
        return result