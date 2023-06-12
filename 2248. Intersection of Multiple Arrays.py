class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:

        set1 = set(nums[0])

        for i in range(1, len(nums)):
            newSet = set(nums[i])
            set1 = set1.intersection(newSet)
        return list(sorted(set1))
