class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        freq = {}
        left = 0
        res = 0
        max_sum = 0
        for right in range(len(nums)):
            
            freq[nums[right]] = freq.get(nums[right], 0) + 1
            
            

            while right-left+1 > k:
                max_sum-=nums[left]
            
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                
                left += 1
            max_sum += nums[right]
            if right-left+1==k and len(freq)==k:
                
                res = max(max_sum, res)
        return res
