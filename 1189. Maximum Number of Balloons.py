class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        ans = [0 for i in range(5)]

        for i in text:
            if i == "b":
                ans[0] += 1
            elif i == "a":
                ans[1] += 1
            elif i == "l":
                ans[2] += 1
            elif i == "o":
                ans[3] += 1
            elif i == "n":
                ans[4] += 1
        
        ans[2] = ans[2] //2
        ans[3] = ans[3] //2

        
        return min(ans)





        
