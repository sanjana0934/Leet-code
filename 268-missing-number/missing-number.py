class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n=len(nums)
        actual=(n*(n+1))//2
        given_sum=sum(nums)
        return actual-given_sum