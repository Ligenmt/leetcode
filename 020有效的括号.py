class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = ['(', '{', '[']
        right = [')', '}', ']']
        l = []
        for i in s:
            if i in left:
                l.append(i)
            if i in right:
                try:
                    currentleft = l.pop()
                except:
                    return False
                if i == ')':
                    if currentleft != '(':
                        return False
                if i == ']':
                    if currentleft != '[':
                        return False
                if i == '}':
                    if currentleft != '{':
                        return False
        if len(l) != 0:
            return False
        return True


print(Solution().isValid("["))
