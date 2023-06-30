class Solution:
    def minStartValue(self, nums: List[int]) -> int:

        ## [-3,2,-3,4,2]
        ## you take the number to be x
        ## [x-3, x-1, x-4, x, x+2]

        ans = [nums[0]]
        for i in range(1, len(nums)):
            ans.append(ans[-1]+ nums[i])
        #print(ans)

        mins = min(ans)
        #print(mins)
        res = 0

        if mins < 0:
            res = abs(mins) + 1
        else:
            res = 1
        return res
