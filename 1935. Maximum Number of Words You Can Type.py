class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:

        arr = text.split(" ")

        def check_valid(word, pattern):
            for i in word:
                if i in pattern:
                    return False
            return True
            
        
        count = 0
        for i in arr:
            if check_valid(i, brokenLetters):
                count += 1
        return count

