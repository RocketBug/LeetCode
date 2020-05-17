#problem url https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        trust_dict = {}
        result = -1
        for i in range(0, len(trust)):
            if trust[i][0] not in trust_dict:
                trust_dict[trust[i][0]] = []
                
            trust_dict[trust[i][0]].append(trust[i][1])
        
        for j in range(1, N+1):
            if j not in trust_dict:
                result = j
                
            
        if result == -1:
            return -1
        
        else:
            for k in trust_dict.keys():
                if result not in trust_dict[k]:
                    return -1
                
            return result