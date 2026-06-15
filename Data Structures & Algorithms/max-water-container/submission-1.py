class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(heights) - 1
        
        while left < right:
            # 1. Calculate current area
            width = right - left
            height = min(heights[left], heights[right])
            current_area = width * height
            
            # 2. Update maximum area found so far (No list needed!)
            if current_area > max_area:
                max_area = current_area
            
            # 3. Move the pointer pointing to the shorter bar
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
                
        return max_area