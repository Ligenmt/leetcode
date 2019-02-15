class Solution:
    def removeElement(self, nums, val):
        """双指针
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i


nums = [0,1,2,2,3,0,4,2]
print(Solution().removeElement(nums, 2))
print(nums)