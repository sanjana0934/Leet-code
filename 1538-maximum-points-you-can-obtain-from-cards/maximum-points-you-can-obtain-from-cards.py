class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        curr_sum=sum(cardPoints[:k])
        res_sum=curr_sum
        left=k-1
        right=len(cardPoints)-1
        while(left>=0 and left<len(cardPoints)):
            
            curr_sum-=cardPoints[left]
            curr_sum+=cardPoints[right]
            left-=1
            right-=1
            res_sum=max(curr_sum,res_sum)
        return res_sum