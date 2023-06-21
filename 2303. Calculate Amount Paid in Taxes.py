class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:

        pay = []

        for i in range(len(brackets)):
            if brackets[i][0] <= income:
                pay.append([brackets[i][0],brackets[i][1]])
            else:
                pay.append([income, brackets[i][1]])
                break
        
        
        ans = [pay[0]]
        for i in range(1, len(pay)):
            ans.append([pay[i][0]-pay[i-1][0], pay[i][1]])
            
        
        tax = 0
        for i in range(len(ans)):
            tax += ans[i][0] * (ans[i][1]/100)
        return tax


        
        
        
        
