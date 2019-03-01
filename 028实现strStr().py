class Solution:
    def strStr(self, haystack, needle):
        """
            示例 1:
            输入: haystack = "hello", needle = "ll"
            输出: 2
            示例 2:
            输入: haystack = "aaaaa", needle = "bba"
            输出: -1

            双指针 KMP
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0
        if len(haystack) == 0:
            return -1

        n = 0  #neddle指针
        h = 0  #haystack指针
        while h < len(haystack):
            if haystack[h] != needle[n]:
                h -= n
                n = 0
            else:
                n += 1
            if n == len(needle):
                return h - n + 1
            h += 1
        return -1


print(Solution().strStr("hello", "ll"))
print(Solution().strStr("mississippi", "issip"))

