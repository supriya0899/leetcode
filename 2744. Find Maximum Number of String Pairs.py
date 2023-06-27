class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:

        rev = []
        rev2 = []
        for i in words:
            rev.append(i[::-1])
        print(rev)
        for i in rev:
            if i[0] != i[1]:
                rev2.append(i)
        print(rev2)
        count = 0
        for i in range(len(words)):
            for j in range(len(rev2)):
                if words[i] == rev2[j]:
                    count +=1
        return (count//2)
