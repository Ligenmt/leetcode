class Solution:
    def longestCommonPrefix(self, strs):
        """
        最长相同前缀
        :type strs: List[str]
        :rtype: str
        """

        prefix = ''
        if len(strs) == 0:
            return prefix
        if len(strs) == 1:
            return strs[0]
        minlen = min([len(word) for word in strs])
        if minlen == 0:
            return ""
        for i in range(minlen):
            flag = True
            for j in range(len(strs)-1):
                if strs[j][i] != strs[j+1][i]:
                    flag = False
                    break
            if flag:
                prefix += strs[0][i]
            else:
                return prefix
        return prefix


print(Solution().longestCommonPrefix(["fefe", "fefefe"]))