class Solution:
    def generateParenthesis(self, n):
        """回溯法
        :type n: int
        :rtype: List[str]
        """
        result = []

        def backtrack(s='', left=0, right=0):
            if len(s) == 2 * n:
                print(s)
                result.append(s)
                return
            if left < n:
                backtrack(s + '(', left+1, right)
            if left > right:
                backtrack(s + ')', left, right+1)
        backtrack()
        return result


print(Solution().generateParenthesis(2))



