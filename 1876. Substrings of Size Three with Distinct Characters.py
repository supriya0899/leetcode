class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        i = 0
        sub = []

        for j in range(len(s)-2):
            sub.append(s[i:j+3])
            i = j+1
        count = 0
        new = []
        for i in sub:
            if len(set(i)) == 3:
                count +=1
            
        return count

