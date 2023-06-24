class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:

        set1 = set(words1)
        set2 = set(words2)

        common = set1.intersection(set2)
        print(common)

        new_set = words1 + words2
        print(new_set)

        dicts = {}

        for i in range(len(new_set)):
            if new_set[i] in common:
                if new_set[i] in dicts:
                    dicts[new_set[i]] += 1
                else:
                    dicts[new_set[i]] = 1
        print(dicts)
        count = 0 
        for i in dicts:
            if dicts[i] == 2:
                count +=1 
        return count


        

        


        
