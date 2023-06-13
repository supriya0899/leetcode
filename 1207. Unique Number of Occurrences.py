class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        dicts = {}
        res = []

        for i in range(len(arr)):
            if arr[i] in dicts:
                dicts[arr[i]] += 1
            else:
                dicts[arr[i]] = 1
        
        for i in dicts:
            res.append(dicts[i])
        if len(res) == len(set(res)):
            return True
        else:
            return False
        
        
        
