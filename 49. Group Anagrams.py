class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dicts = collections.defaultdict(list)

        for i in strs:
            sortedWord = "".join(sorted(i))
            dicts[sortedWord].append(i)

        res = []
        for i in dicts.values():
            res.append(i)
        return res



        

        

        

        








    



        
            



     
