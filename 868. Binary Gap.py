class Solution:
    def binaryGap(self, n: int) -> int:

        temp = format(n, "b")
        #print(temp)
        ans = []

        for i in range(len(temp)):
            if temp[i] == "1":
                ans.append(i)
        #print(ans)

        if len(ans) <= 1:
            return 0
        
        maxi = 0
        for i in range(len(ans)-1):
            maxi = max(maxi, int(ans[i+1]- int(ans[i])))
        return maxi


       
