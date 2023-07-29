class Solution:
    def isValid(self, s: str) -> bool:

        dicts = {"}":"{", ")":"(", "]":"["}

        stack = []

        for i in s:
            if i in dicts:
                if stack and stack[-1] == dicts[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
                
        #print(stack)
        
        if stack:
            return False
            
        else:
            return True
