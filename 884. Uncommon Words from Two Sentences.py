class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:

        new_s1 = s1.split(" ")
        new_s2 = s2.split(" ")
        combo = new_s1 + new_s2
        print(combo)
        
        dicts = {}
        for i in combo:
            if i in dicts:
                dicts[i] += 1
            else:
                dicts[i] = 1
        
        ans = []
        for i in dicts:
            if dicts[i] < 2:
                ans.append(i)
        return ans
