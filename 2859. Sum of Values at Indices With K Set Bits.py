class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        
        res = []
        for i in range(len(nums)):
            temp = format(i, "b")
            res.append(temp.count("1"))
        
        count = 0
        for i in range(len(res)):
            if res[i] == k:
                count += nums[i]
        return count

        
