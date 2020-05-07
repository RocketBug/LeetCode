from collections import Counter
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        result = 0
        c = Counter(S)
        for j in J:
            if j in c:
                result += c[j]
                
        return result
                    