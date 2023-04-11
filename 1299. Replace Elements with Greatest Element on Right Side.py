class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        new = [-1]
        max = 0
        for i in range(len(arr)-1, -1,-1):
            if max < arr[i]:
                max = arr[i]
            new.append(max)
        new.pop()
        return new[::-1]
