class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:

        dicts = {}
        ans = []

        for i in range(len(arr)):
            if arr[i] in dicts:
                dicts[arr[i]] += 1
            else:
                dicts[arr[i]] = 1
        
        for i in dicts:
            if dicts[i] == 1:
                ans.append([i, dicts[i]])
        
        if len(ans) <k:
            return ""
        return ans[k-1][0]



        



