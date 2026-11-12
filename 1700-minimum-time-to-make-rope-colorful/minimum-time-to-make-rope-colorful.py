class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        m=len(colors)
        time=0
        max_value=0
        prev=neededTime[0]
        
        for i in range (1,m):
            if colors[i]==colors[i-1]:
                time+=min(prev,neededTime[i])
                prev=max(neededTime[i],prev)
            else:
                prev=neededTime[i]
        return time

            
        
        