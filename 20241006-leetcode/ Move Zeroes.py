# Python script for LeetCode problems
# correct solution
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_index = 0  
        index = 0  

        while index < len(nums):
            if nums[index] != 0:
                nums[non_zero_index], nums[index] = nums[index], nums[non_zero_index]
                non_zero_index += 1
            index += 1