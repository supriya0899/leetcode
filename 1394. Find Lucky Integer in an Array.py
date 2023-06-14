class Solution:
    def findLucky(self, arr: List[int]) -> int:

        dicts = {}

        for i in range(len(arr)):
            if arr[i] in dicts:
                dicts[arr[i]] += 1
            else:
                dicts[arr[i]] = 1
        
        ans = []
        for i in dicts:
            if i == dicts[i]:
                ans.append(i)
            
        if ans:
            return max(ans)
        else:
            return -1
            

        
        
