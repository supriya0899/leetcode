class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:

        dicts = {}
        for i in range(len(nums)):
            if nums[i] in dicts:
                dicts[nums[i]] += 1
            else:
                dicts[nums[i]] = 1
        
        ans = []
        for i in dicts:
            ans.append([i, dicts[i]])

        ans = sorted(ans, reverse = True, key = lambda x:(x[1]))

        return target == ans[0][0] and ans[0][1] > len(nums)/2
        




        
            
