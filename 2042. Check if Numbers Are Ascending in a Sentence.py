class Solution:
    def areNumbersAscending(self, s: str) -> bool:

        ans = []
        s = s.split(" ")

        for i in range(len(s)):
            if s[i].isdigit():
                ans.append(int(s[i]))
        
        for i in range(len(ans)-1):
            if ans[i] >= ans[i+1]:
                return False
        return True
