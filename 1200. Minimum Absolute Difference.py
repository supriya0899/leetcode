class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:

        res = []
        ans = []
        arr.sort()
        print(arr)
        for i in range(len(arr)-1):
            res.append(arr[i+1]-arr[i])
        
        diff = min(res)

        for i in range(len(arr)-1):
            if (arr[i+1]- arr[i]) == diff:
                ans.append([arr[i], arr[i+1]])
        return ans
