class Solution:
    def reverseBits(self, n: int) -> int:

        num = format(n, "b")
        temp = int(num, 2)

        num2 = format(temp, "b")
        
        num2 = num2[::-1]

        temp2 = "".join(num2)

        while len(temp2) < 32:
            temp2 += "0"

        #print(temp2)

        
        return int(temp2, 2)

        
        

       
   
        
