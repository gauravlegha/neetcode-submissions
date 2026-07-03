class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = [-1] # Initialize with -1 to easily calculate width for the first element
        max_area = 0
    
        for i, h in enumerate(heights):
            # While the current bar is shorter than the bar at the top of the stack
            while stack[-1] != -1 and heights[stack[-1]] >= h:
                # The popped bar is the minimum height of the rectangle we are evaluating
                current_height = heights[stack.pop()]
                
                # The width is the distance between the current index and the new top of the stack
                current_width = i - stack[-1] - 1
                
                # Update the maximum area found so far
                max_area = max(max_area, current_height * current_width)
                
            # Push the current index onto the stack
            stack.append(i)
            
        # Remove the dummy 0 we added to keep the original array intact
        heights.pop()
        
        return max_area