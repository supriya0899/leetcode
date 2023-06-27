class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:

        sub = []

        i =0
        for j in range(len(s)):
            sub.append(s[i:j+1])
        print(sub)

        count = 0 
        for i in words:
            if i in sub:
                count += 1
        return count

