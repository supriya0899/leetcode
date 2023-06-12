class Solution:
    def maximumCount(self, nums: List[int]) -> int:

        pos, neg = [], []
        for i in range(len(nums)):
            if nums[i] < 0:
                neg.append(nums[i])
            elif nums[i] > 0:
                pos.append(nums[i])
        
        
        if len(pos) >= len(neg):
            return len(pos)
        else:
            return len(neg)
