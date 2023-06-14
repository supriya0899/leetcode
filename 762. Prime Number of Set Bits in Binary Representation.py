class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:

        binary = []

        for i in range(left, right+1):
            binary.append(format(i, "b"))
        

        ans = []

        for x in binary:
            ans.append(x.count('1'))
        
        def prime_check(num):
            if num == 1:
                return False
            
            for i in range(2, num):
                if num % i == 0:
                    return False
            return True

        count = 0
        for i in ans:
            if prime_check(i):
                count += 1
        return count

        
       
        
         











            
            

            
        
        


        
        
        
            
