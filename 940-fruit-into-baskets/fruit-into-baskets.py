class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        k=2
        freq={}
        left=0
        res=0
        for right in range (len(fruits)):
            freq[fruits[right]]=freq.get(fruits[right],0)+1
            
            while len(freq)>k:
                freq[fruits[left]] -= 1
                if freq[fruits[left]]==0:
                    del freq[fruits[left]]
                   
                left+=1
            total=right-left+1
            res=max(res,total)
           
        return res




        