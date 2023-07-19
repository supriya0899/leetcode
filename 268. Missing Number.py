class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        ans = [-1 for i in range(len(nums)+1)]
        #print(ans)
        
        for i in range(len(nums)):
            ans[nums[i]] = nums[i]
        print(ans)
        

        return ans.index(-1)



        



        
        
