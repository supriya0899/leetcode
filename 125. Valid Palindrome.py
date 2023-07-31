class Solution:
    def isPalindrome(self, s: str) -> bool:

        ans = ""
        for i in s:
            if i.isalnum():
                ans+= i.lower()
        #print(ans)
        
        return ans == ans[::-1]


        
       



      
        
