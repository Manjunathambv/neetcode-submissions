class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum_array = []
        self.prefix_sum = 0
        for i in range(len(nums)):
            self.prefix_sum += nums[i]
            self.prefix_sum_array.append(self.prefix_sum)
        

    def sumRange(self, left: int, right: int) -> int:
        right_sum = self.prefix_sum_array[right]
        left_sum = self.prefix_sum_array[left-1] if left != 0 else 0
        range_sum = right_sum - left_sum
        return range_sum
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)