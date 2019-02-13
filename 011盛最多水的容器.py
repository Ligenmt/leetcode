class Solution:
    def maxArea(self, height):
        """双指针法
        我们在由线段长度构成的数组中使用两个指针，一个放在开始，一个置于末尾。
        使用变量 maxareamaxarea 来持续存储到目前为止所获得的最大面积。
        在每一步中，我们会找出指针所指向的两条线段形成的区域，更新 maxareamaxarea，
        并将指向较短线段的指针向较长线段那端移动一步。
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        area = 0
        i = 0
        j = n-1
        while i != j:
            a1 = height[i]
            a2 = height[j]
            h = min(a1, a2)
            w = j - i
            if h * w > area:
                area = h * w
            if a1 > a2:
                j -= 1
            else:
                i += 1
        return area


print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))
