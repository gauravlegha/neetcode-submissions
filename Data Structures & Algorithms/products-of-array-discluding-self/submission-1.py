class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out=[]
        for i in range(len(nums)):
            l=1
            for j in range(len(nums)):
                if j==i:
                    continue
                l*=nums[j]
            out.append(l)
        return out