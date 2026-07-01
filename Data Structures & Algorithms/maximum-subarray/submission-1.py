class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cursum = 0
        maxsum = nums[0]
        L, R = 0, 0
        maxL, maxR = 0, 0
        while R < len(nums):
            if cursum < 0:
                cursum = 0
                L = R
            cursum += nums[R]
            if cursum > maxsum:
                maxsum = cursum
                maxL = L
                maxR = R
            R += 1
        return maxsum