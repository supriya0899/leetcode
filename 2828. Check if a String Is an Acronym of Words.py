class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        res = []

        for word in words:
            for i in word:
                res.append(i)
                break
        return True if "".join(res) == s else False
