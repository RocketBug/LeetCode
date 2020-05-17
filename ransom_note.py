#problem url https://leetcode.com/problems/ransom-note/
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNoteCounter = Counter(ransomNote)
        magazineCounter = Counter(magazine)
        
        for rk in ransomNoteCounter.keys():
            if magazineCounter[rk] < ransomNoteCounter[rk]:
                return False
            
            
        return True