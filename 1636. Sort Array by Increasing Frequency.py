class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:

        dict = {}
        res = []

        for i in range(len(nums)):
            if nums[i] in dict:
                dict[nums[i]] += 1
            else:
                dict[nums[i]] = 1
        
        for key in dict:
            res.append([key, dict[key]])
        
        res = sorted(res, key = lambda x:(x[1], -x[0]))
        ans = [] 
        for num, cnt in res:
            for x in range(cnt):
                ans.append(num)
        
        
        
        return ans
            
        

       
