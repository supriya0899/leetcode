class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        new = set(nums)
        #print(new)

        if len(new) != len(nums):
            return True
        else:
            return False



            
        
