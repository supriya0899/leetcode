class Solution:
    def alternateDigitSum(self, n: int) -> int:

        num = list(str(n))

        ans1, ans2 = [], []

        for i in range(len(num)):
            if i %2 == 0:
                ans1.append(int(num[i]))
            else:
                ans2.append(int(num[i]))
        
        return sum(ans1) - sum(ans2)
                
        
