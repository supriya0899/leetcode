class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

        

        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                continue
            else:
                nums[i] = nums[i]*2
                nums[i+1] = 0

        digit = []
        zeroes = []
        for i in nums:
            if i != 0:
                digit.append(i)
            else:
                zeroes.append(i)
        return digit + zeroes
