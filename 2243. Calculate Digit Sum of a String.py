class Solution:
    def digitSum(self, s: str, k: int) -> str:
        def digitsum(v):
            sums = 0
            for i in v:
                sums += int(i)
            return str(sums)
        
        while len(s) > k:

            ans = []
            for i in range(0, len(s), k):
                ans.append(s[i:i+k])
                
            

            res = ""
            for i in ans:
                res += digitsum(i)
            s = res
        return s


        
