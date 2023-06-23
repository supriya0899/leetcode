class Solution:
    def similarPairs(self, words: List[str]) -> int:

        ans = []

        for i in range(len(words)):
            ans.append(set(words[i]))
        print(ans)

        count = 0

        for i in range(len(ans)-1):
            for j in range(i+1, len(ans)):
                if ans[i] == ans[j]:
                    count += 1
        return count



    
