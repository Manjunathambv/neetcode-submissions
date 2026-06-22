class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0

        sum_ = 0
        max_sum = 0
        i = 0
        while i < len(nums):
            if nums[i] == 1:
                sum_ += 1
            else:
                sum_ = 0
            max_sum = max(sum_, max_sum)
            i += 1
        return max_sum
        