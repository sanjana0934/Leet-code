class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        freq={}
        max_freq=0
        left=0
        for right in range (len(answerKey)):
            freq[answerKey[right]]=freq.get(answerKey[right],0)+1
            while min(freq.get('T',0),freq.get('F',0))>k:
                freq[answerKey[left]]-=1
                
                if freq[answerKey[left]]==0:

                    del freq[answerKey[left]]
                left+=1
            max_freq=max(max_freq,right-left+1)
        return max_freq
                

                