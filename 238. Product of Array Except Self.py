class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        pre = [1]
        post = [1]

        for i in range(len(nums)-1):
            pre.append(pre[-1] * nums[i])
        #print(pre)

        for i in nums[::-1][:-1]:
            post.append(post[-1]*i)
        post = post[::-1]
        #print(post)

        res = []
        for i in range(len(pre)):
            res.append(pre[i]*post[i])
        return res
