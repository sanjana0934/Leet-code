class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        freq={}
        left=0
        max_freq=0
        for right in range (len(nums)):
            freq[nums[right]]=freq.get(nums[right],0)+1
            while 0 in freq and freq[0]>k:
                freq[nums[left]]-=1
                if freq[nums[left]]==0:
                    del freq[nums[left]]
                left+=1
            max_freq=max(max_freq,right-left+1)
        return max_freq


           
         

        