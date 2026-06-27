class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxl=[]
        for i in range(len(nums)-k +1):
            s=nums[i:i+k]
            maxl.append(max(s))
        return maxl
            