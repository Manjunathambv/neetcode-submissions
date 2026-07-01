class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        right_max_array = [0] * n
        right_max_array[-1] = nums[-1]
        right_sum = nums[-1]

        for i in range(n-2, -1, -1):
            right_sum = right_sum + nums[i]
            right_max_array[i] = max(right_sum, right_max_array[i+1])

        cir_max_sum = nums[-1]
        max_sum = nums[-1]
        pref_sum = 0
        cur_sum = 0
        for i in range(0,n):
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += nums[i]
            pref_sum += nums[i]
            if cur_sum > max_sum:
                max_sum = cur_sum
            if i+1 < n:
                cir_max_sum = max(max_sum, pref_sum + right_max_array[i+1], cir_max_sum)

        return cir_max_sum
        