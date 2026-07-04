class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        max_height=0
        stack=[-1]
        for curr_idx, current_height in enumerate(heights):
            while stack[-1]!=-1 and heights[stack[-1]]>=current_height:
                popped_plank_height = heights[stack.pop()]
                width=curr_idx-stack[-1]-1
                area=popped_plank_height*width
                max_height=max(max_height,area)
            stack.append(curr_idx)
        return max_height
                