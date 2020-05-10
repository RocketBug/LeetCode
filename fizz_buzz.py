#problem url https://leetcode.com/problems/fizz-buzz/
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        value = []
        for i in range(1, n+1):
            if i%3 == 0 and i%5 == 0:
                value.append("FizzBuzz")
            elif i%3 == 0:
                value.append("Fizz")
            elif i%5 == 0:
                value.append("Buzz")
            else:
                value.append(str(i))
                
            
        return value
                
            