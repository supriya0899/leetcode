class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:

        rank = []

        for i in range(len(score)):
            rank.append([score[i], i])
        

        rank = sorted(rank, reverse = True, key= lambda x:x[0])
        

        rank[0].append("Gold Medal")
        if len(rank) >= 2:
            rank[1].append("Silver Medal")
        if len(rank) >=3:
            rank[2].append("Bronze Medal")
        print(rank)
        
        ans = [0 for x in range(len(score))]
        
        for i in range(len(rank)):
            if len(rank[i]) == 3:
                ans[rank[i][1]] = rank[i][2]
            else:
                ans[rank[i][1]] = str(i+1)
        return ans

        









        
        

        
