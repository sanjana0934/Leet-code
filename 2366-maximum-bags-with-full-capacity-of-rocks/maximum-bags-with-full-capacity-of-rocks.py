class Solution:
    def maximumBags(self, capacity: list[int], rocks: list[int], additionalRocks: int) -> int:
        required=[]
        count=0
        for i in range (len(rocks)):
            required.append(capacity[i]-rocks[i])
        required.sort()
        [1,1,0,1]
        for i in required:
            if additionalRocks>=i:
                additionalRocks-=i
                count+=1
            else:
                break
            
        return count

            



        
        