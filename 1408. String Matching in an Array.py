class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:

        ans = []
        
        for i in range(len(words)):
            for j in range(len(words)):
                if words[j] in words[i] and i != j:
                    if words[j] not in ans:
                        ans.append(words[j])
        return ans

