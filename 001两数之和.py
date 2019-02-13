def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    nummap = {}
    for i in range(len(nums)):
        nummap[nums[i]] = i
    for i in range(len(nums)):
        complement = target - nums[i]
        if nummap.get(complement) and nummap[complement] != i:
            return [i, nummap[complement]]


def twoSum2(nums, target):
    m = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if m.__contains__(complement):
            return [m[complement], i]
        m[nums[i]] = i


numbers = [2, 7, 11, 15]
_target = 9
print(twoSum2(numbers, _target))
