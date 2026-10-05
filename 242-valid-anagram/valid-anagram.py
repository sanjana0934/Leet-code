class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        freq={}
        for i in s:
            freq[i]=freq.get(i,0)+1
        for j in t:
            if j in freq:
                freq[j]-=1
                if freq[j]==0:
                    del[freq[j]]
        return not freq
            

        