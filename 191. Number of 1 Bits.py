class Solution:
    def hammingWeight(self, n: int) -> int:

        num = format(n, "b")
        count = 0
        
        for i in num:
            if i == "1":
                count += 1
        return count


        




        
        
        
        
