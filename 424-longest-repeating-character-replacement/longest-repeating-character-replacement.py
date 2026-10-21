class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        max_freq=0
        count={}
        result=0
        for right in range(len(s)):
            count[s[right]]=count.get(s[right],0)+1
            max_freq=max(max_freq,count[s[right]])
            sliding_window=right-left+1
            replacement=sliding_window-max_freq
            if replacement>k:
                count[s[left]]-=1
                left+=1
            result=max(result,right-left+1)
        return result