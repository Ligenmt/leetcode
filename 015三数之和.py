class Solution:
    def threeSum(self, nums):
        """三数之和
        1.将数组排序
        2.定义三个指针，i，j，k。遍历i，
        那么这个问题就可以转化为在i之后的数组中寻找nums[j]+nums[k]=-nums[i]这个问题，也就将三数之和问题转变为二数之和
        可以使用双指针
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        solution = []
        nums.sort()
        print(nums)
        i = 0
        for i in range(len(nums)):
            if i == 0 or nums[i] > nums[i-1]:
                j = i + 1
                k = len(nums) - 1
                while j < k:
                    s = nums[i] + nums[j] + nums[k]
                    if s == 0:
                        solution.append([nums[i], nums[j], nums[k]])
                        j += 1
                        k -= 1
                        while j < k and nums[j] == nums[j-1]:
                            j += 1
                        while j < k and nums[k] == nums[k+1]:
                            k -= 1
                    elif s > 0:
                        k -= 1
                    else:
                        j += 1
        return solution


# print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
print(Solution().threeSum([-2, 0, 0, 2, 2]))
