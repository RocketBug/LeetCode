# problem url https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        elif N == 1 or N == 2:
            return 1
        else:
            arr = [0 for i in range(N)]
            arr[0] = 1
            arr[1] = 1
            for i in range(2, N):
                arr[i] = arr[i-2] + arr[i-1]
                
            return arr[-1]
        