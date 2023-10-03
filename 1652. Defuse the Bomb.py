class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        
        if k >0:
            final = code + code[:k]
            for i in range(len(code)):
                code[i] = sum(final[i+1:i+1+k])
            return code
        if k == 0:
            for i in range(len(code)):
                code[i] = 0
            return code
        else:
            code = code[::-1]
            k = -1 * k
            final = code + code[:k]
            for i in range(len(code)):
                code[i] = sum(final[i+1:i+1+k])
            code = code[::-1]
            return code

