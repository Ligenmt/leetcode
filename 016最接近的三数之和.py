class Solution:
    def threeSumClosest(self, nums, target):
        """双指针
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()

        i = 0
        closeSum = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)):
            j = i+1
            k = len(nums)-1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                diff = abs(target - s)  #目前的差
                lastdiff = abs(target - closeSum)  #之前的差
                if diff < lastdiff:
                    closeSum = s
                if s > target:
                    k -= 1
                elif s < target:
                    j += 1
                else:
                    return target
        return closeSum


print(Solution().threeSumClosest([-1,2,1,-4], 1))