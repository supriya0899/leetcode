class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()
        ans = ""
        
        for i in s:
            if (ord("a") <= ord(i) <= ord("z") or ord("0")<= ord(i) <= ord('9')):
                ans += i
        return ans == ans[::-1]
