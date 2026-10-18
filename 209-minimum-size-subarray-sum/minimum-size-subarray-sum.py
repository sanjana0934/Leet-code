class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        sum=0
        min_subarray=float("inf")
        left=0
        
        for right in range(len(nums)):
            sum+=nums[right]
            while(sum>=target):
                min_subarray=min(min_subarray,right-left+1)
                sum-=nums[left]
                left+=1
            right+=1
        if min_subarray==float("inf"):
            return 0
        else:
            return min_subarray
        