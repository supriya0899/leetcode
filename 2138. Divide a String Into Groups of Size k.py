class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:

        
        new = []

        for i in range(0,len(s), k):
            new.append(s[i:i+k])
        
        while len(new[-1]) != k:
            new[-1] += fill
        return new



        #print(new)
