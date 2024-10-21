# Python script for LeetCode problems
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        # 初始化前 k 個元素的總和
        current_sum = sum(nums[:k])
        max_sum = current_sum

        # 使用滑動窗口遍歷陣列
        for i in range(k, len(nums)):
            # 更新當前窗口的總和
            current_sum += nums[i] - nums[i - k]
            # 更新最大總和
            max_sum = max(max_sum, current_sum)

        # 返回最大平均值
        return max_sum / k
