class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dicts = {}
        ans = []

        for i in range(len(nums)):

            dicts[nums[i]] = 1 + dicts.get(nums[i], 0)
        

        for i in dicts:
            ans.append([i, dicts[i]])

        ans = sorted(ans, key = lambda x:x[1], reverse = True)
        

        res = []
        for i in range(k):
            res.append(ans[i][0])
        return res
