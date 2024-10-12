class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        
        while left < right:
            # 計算當前的面積
            current_area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, current_area)
            
            # 移動指向較短邊的指針
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
