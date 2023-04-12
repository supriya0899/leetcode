class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:

        seen, res = set(), set()

        for r in range(len(s)-9):
            cur = s[r:r+10]
            if cur in seen:
                res.add(cur)
            else:
                seen.add(cur)
        return list(res)

