class Solution:
    def countEven(self, num: int) -> int:
        
        count = 0
        for i in range(1, num+1):
            s = str(i)
            ans = 0
            for x in s:
                ans += int(x)
            if ans %2 == 0:
                count +=1
        return count
