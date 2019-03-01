class Solution:
    def searchInsert(self, nums, target):
        """二分法
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        beg = 0
        end = len(nums)
        while beg < end:
            mid = beg + (end - beg) // 2
            print(mid, beg, end)
            if target < nums[mid]:
                end = mid
            elif target > nums[mid]:
                beg = mid + 1
            else:
                return mid
        return beg


print(Solution().searchInsert([1,3,5,6], 7))