class Solution:
    def findMaxK(self, nums: List[int]) -> int:

        ans = []

        for i in range(len(nums)):
            if nums[i] and -nums[i] in nums:
                ans.append(nums[i])
                
        
            
        ans.sort(reverse= True)
        
        return ans[0] if ans else -1
                
        
        
