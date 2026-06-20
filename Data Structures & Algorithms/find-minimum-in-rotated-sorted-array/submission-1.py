class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        while l<r:
            mid=(l+r)//2

            if nums[mid]>nums[r]:
                l=mid+1 
            else:r=mid 
        return nums[l] 
            
            #mid=l+(r-l)//2
            #if abs(nums[mid+1]-nums[mid])>1:
                #return nums[mid+1]
            #elif abs(nums[mid]-nums[mid-1])>1:
                #return nums[mid]
            
            