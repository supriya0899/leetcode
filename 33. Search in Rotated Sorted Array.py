class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l+r)//2

            if target == nums[mid]:
                return mid
            #leftmost
            if nums[mid] >= nums[l]:
                if target > nums[mid] or nums[l] > target:
                    l = mid +1
                else:
                    r = mid -1
            #rightmost
            else:
                if target < nums[mid] or nums[r] < target:
                    r = mid -1
                else:
                    l = mid +1
        return -1
