class Solution:
    def lengthOfLastWord(self, s):
        """
        这题有点蠢
        :type s: str
        :rtype: int
        """
        n = 0
        result = 0
        for i in range(len(s)):
            c = s[i]
            if c == ' ':
                if n != 0:
                    result = n
                n = 0
            else:
                n += 1
        if n != 0:
            result = n
        return result


print(Solution().lengthOfLastWord("a"))

