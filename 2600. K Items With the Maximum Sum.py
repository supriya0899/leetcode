class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:

        ans = []

        while numOnes >0:
            ans.append(1)
            numOnes -= 1
        while numZeros >0:
            ans.append(0)
            numZeros -= 1
        while numNegOnes:
            ans.append(-1)
            numNegOnes -= 1
        
        res = 0
        for i in range(k):
            res += ans[i]
        return res
