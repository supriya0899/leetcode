class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:

        nums = sorted(nums, key = lambda x:x[0])
       
        res = [nums[0]]

        for i in range(1, len(nums)):
            if res[-1][1] >= nums[i][0]:
                res[-1][1] = max(res[-1][1], nums[i][1])
            else:
                res.append(nums[i])
        print(res)
        ans = 0
        for i in range(len(res)):
            ans += res[i][1] - res[i][0]
        return ans + len(res)
        

        



        
