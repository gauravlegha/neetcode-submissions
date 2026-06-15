class Solution:
    def maxArea(self, heights: List[int]) -> int:
        areal=[]
        h=0
        w=0
        area=0
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                h=min(heights[j],heights[i])
                w=abs(j-i)
                area=h*w
                areal.append(area)
        return max(areal)