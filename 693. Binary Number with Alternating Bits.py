class Solution:
    def hasAlternatingBits(self, n: int) -> bool:

        convert = format(n, "b")
        #print(convert)

        for i in range(len(convert)-1):
            if convert[i+1] == convert[i]:
                return False
        return True


            



