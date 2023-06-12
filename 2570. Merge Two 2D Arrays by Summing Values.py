class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:

        arr = nums1 + nums2
        ans = []

        dicts = {}

        for i in range(len(arr)):
            if arr[i][0] in dicts:
                dicts[arr[i][0]] += arr[i][1]
            else:
                dicts[arr[i][0]] = arr[i][1]
        
        for i in dicts:
            ans.append([i, dicts[i]])
        ans = sorted(ans, key = lambda x:(x[0]))
        return ans
