class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        left = 0
        count = 0
        # Hash map to maintain the frequency of elements in the current window
        freq = {}
        
        for right in range(len(nums)):
            # Add the current element to the window
            freq[nums[right]] = freq.get(nums[right], 0) + 1
            
            # Shrink the window if max(window) - min(window) > 2
            while max(freq) - min(freq) > 2:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1
                
            # Add the number of valid subarrays ending at the 'right' index
            count += (right - left + 1)
            
        return count
