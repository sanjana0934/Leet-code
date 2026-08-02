class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        last_end=points[0][1]
        count=1
        for start,end in points[1:]:
            if start>last_end:
                count+=1
                last_end=end
        return count
            
            


