class Solution:
    def trimMean(self, arr: List[int]) -> float:

        arr.sort()
        print(arr)
        

        cal = int(len(arr) *(5/100))
        #print(cal)

        for i in range(cal):
            arr.remove(min(arr))
            arr.remove(max(arr))
        return sum(arr) / len(arr)
