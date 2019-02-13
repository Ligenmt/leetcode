class Solution:
    def letterCombinations(self, digits):
        """回溯 + 递归
        :type digits: str
        :rtype: List[str]
        """
        keyboard = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        solition = set()
        array = []
        for digit in digits:
            x = keyboard[digit]
            array.append(x)
        solution = []
        solution = self.getStringWithFor(array, 0, solution, '')
        return solution

    def getStringWithFor(self, arr, index, solution, stemp):

        if index < len(arr)-1:
            for j in range(len(arr[index])):
                solution = self.getStringWithFor(arr, index + 1, solution, stemp + arr[index][j])
        else:
            for j in range(len(arr[index])):
                solution.append(stemp + arr[index][j])
        return solution


print(Solution().letterCombinations("23"))
