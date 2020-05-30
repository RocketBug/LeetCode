# https://leetcode.com/problems/sort-characters-by-frequency/
from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        ctr = Counter(s)
        most = ctr.most_common()
        res = ""
        for i in most:
            res += i[0] * i[1]
            
        return res
        