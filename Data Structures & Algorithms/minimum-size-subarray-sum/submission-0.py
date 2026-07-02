class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L, R = 0, 0
        sum = 0
        minL = float("inf")

        for R in range(len(nums)):
            sum += nums[R]
            while sum >= target:
                minL = min(minL, R-L + 1)
                sum -= nums[L]
                L += 1
        return 0 if minL == float("inf") else minL
        