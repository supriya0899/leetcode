class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        inc = sorted(nums)
        dec = sorted(nums, reverse = True)

        if inc == nums or dec == nums:
            return True
        else:
            return False



                    
