class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        L = 0
        has_set = set()
        for R in range(n):
            if abs(L-R) > k:
                has_set.remove(nums[L])
                L += 1
            if nums[R] in has_set:
                return True
            has_set.add(nums[R])
        return False
        