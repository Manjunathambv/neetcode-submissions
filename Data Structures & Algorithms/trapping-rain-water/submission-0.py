class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = [0] * len(height)
        maxR = [0] * len(height)
        max_left = 0
        max_right = 0
        res = 0
        for i in range(len(height)):
            maxL[i] = max(max_left, height[i])
            max_left = maxL[i]

        for j in range(len(height) - 1, -1, -1):
            maxR[j] = max(max_right, height[j])
            max_right = maxR[j]

        for i in range(len(height)):
            res += min(maxR[i], maxL[i]) - height[i]

        return res
        