class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        new_length = 2 * n
        new_array = [0] * new_length
        i = 0
        while i <= n-1:
            new_array[i] = nums[i]
            new_array[i+n] = nums[i]
            i+=1

        return new_array
        