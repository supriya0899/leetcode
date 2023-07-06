class Solution:
    def isFascinating(self, n: int) -> bool:

        merge_num = str(n) + str(2*n) + str(3*n)

        if len(set(merge_num)) == 9 and len(merge_num) == 9 and "0" not in merge_num:
            return True
        else:
            return False

 
