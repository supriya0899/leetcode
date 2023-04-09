class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        count = 0
        for i in range(len(nums)-1):
            if nums[i+1] == nums[i]:
                count += 1
                nums[i] = float('inf')
        nums.sort()
        return len(nums) - count
