class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:

        seen = set()
        for i in range(len(arr)):
            if (arr[i]/2) in seen or (2*arr[i]) in seen:
                return True
            else:
                seen.add(arr[i])
        return False
