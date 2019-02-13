class Solution:
    def romanToInt(self, s):
        """
        罗马数字转阿拉伯数字
        I can be placed before V (5) and X (10) to make 4 and 9.
        X can be placed before L (50) and C (100) to make 40 and 90.
        C can be placed before D (500) and M (1000) to make 400 and 900.
        这种小在大前面只会出现一次
        :type s: str
        :rtype: int
        """
        total = 0
        if 'IV' in s:
            total -= 2
        if 'IX' in s:
            total -= 2
        if 'XL' in s:
            total -= 20
        if 'XC' in s:
            total -= 20
        if 'CD' in s:
            total -= 200
        if 'CM' in s:
            total -= 200
        for c in s:
            if c == 'I':
                total += 1
            if c == 'V':
                total += 5
            if c == 'X':
                total += 10
            if c == 'L':
                total += 50
            if c == 'C':
                total += 100
            if c == 'D':
                total += 500
            if c == 'M':
                total += 1000
        return total


print(Solution().romanToInt('MCMXCIV'))

