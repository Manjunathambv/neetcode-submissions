class Solution:
    def numOfSubarrays(self, nums: List[int], k: int, threshold: int) -> int:
        L=0
        sub_array = []
        n = len(nums)
        sums = 0
        for i in range(k):
            sums += nums[i]
        for R in range(k, n + 1):
            if (sums // k) >= threshold:
                sub_array.append(nums[L:L + k])
            if R < n:
                sums -= nums[L]
                sums += nums[R]
                L += 1
        return len(sub_array)
            