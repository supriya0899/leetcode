class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cnt = 0 
        n = len(nums)
        for x in range(len(nums)):
            if nums[x] == val:
                cnt+=1
                nums[x] = float('inf')
                
                
        nums.sort()
        return n - cnt
            
