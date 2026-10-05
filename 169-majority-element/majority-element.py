class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        freq={}
        greatest=0
        for i in nums:
            freq[i]=freq.get(i,0)+1
        for i in range (len(nums)):
            num=nums[i]
            if freq[num]>len(nums)//2:
                return num



        