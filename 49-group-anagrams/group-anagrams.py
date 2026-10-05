class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        freq={}
        for i in strs:
            key=''.join(sorted(i))
            if key not in freq:
                freq[key]=[]
            freq[key].append(i)
        return list(freq.values())
        