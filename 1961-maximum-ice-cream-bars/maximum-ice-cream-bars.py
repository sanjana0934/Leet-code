class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        count=0  
        sum=0
        costs.sort()
        for cost in costs:
            if cost<=coins:
                coins-=cost
                count+=1
            else:
                break
        return count
        