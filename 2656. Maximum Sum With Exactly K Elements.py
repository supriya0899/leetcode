class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:

        total = 0

        m = max(nums)
        while k:
            total += m
            m += 1
            k -=1
        return total
