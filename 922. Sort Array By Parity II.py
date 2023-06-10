class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:

        even, odd = [], []
        for i in range(len(nums)):
            if nums[i] %2 == 0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        ans = []
        res = even+ odd
        l, r = 0 , len(res)-1
        while l <= r:
            ans.append(res[l])
            ans.append(res[r])
            l += 1
            r -= 1
        return ans
            

        
        
