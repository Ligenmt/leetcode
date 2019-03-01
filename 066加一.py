class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if len(digits) == 0:
            return [1]
        if digits[0] == 0:
            return [1]
        s = 0
        for i in range(len(digits)):
            s += digits[i] * 10 ** (len(digits) - 1 - i)
        s += 1
        result = []
        for c in str(s):
            result.append(int(c))
        return result
    

print(Solution().plusOne([0]))


