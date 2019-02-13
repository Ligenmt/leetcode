class Solution:
    def isPalindrome(self, x):
        """
        看是不是对称数字
        逐个比较就行了
        另一种算法：取一半反过来和后一半比
        :type x: int
        :rtype: bool
        """
        sx = str(x)
        length = len(sx)
        middle = int(length / 2)
        for i in range(middle):
            if sx[i] != sx[length-1-i]:
                return False
        return True


s = Solution()
print(s.isPalindrome(12212))