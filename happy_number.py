#problem url https://leetcode.com/problems/happy-number/
class Solution:
    def pdi(self, number):
        base = 10
        total = 0
        while number > 0:
            total = total + pow(number%base, 2)
            number = number // base
        return total
    
    def isHappy(self, number: int) -> bool:
        seen = {}
        while number > 1 and number not in seen:
            seen[number] = number
            number = self.pdi(number)
        
        return number == 1