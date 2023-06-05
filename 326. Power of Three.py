class Solution:
    def isPowerOfThree(self, n: int) -> bool:

        if n == 0:
            return False

        done = True
        num = 3

        while done:
            if n % num ==0:
                n = n //num
            else:
                done = False
        
        return n == 1

