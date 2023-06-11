class Solution:
    def countBits(self, n: int) -> List[int]:

        res = []
        for i in range(0,n+1):
            bins = format(i, "b")
            res.append(bins)
   
        final = []
        for i in res:
            final.append(i.count('1'))
        return final
