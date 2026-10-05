class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1, freq2 = {}, {}
        for c in s1:
            freq1[c] = freq1.get(c, 0) + 1
        
        l = 0
        for r in range(len(s2)):
            curr = s2[r]
            freq2[curr] = freq2.get(curr, 0) + 1
            if (r - l + 1) > len(s1):
                freq2[s2[l]] -= 1
                if freq2[s2[l]] == 0:
                    del freq2[s2[l]]
                l += 1
            
            if freq2 == freq1:
                return True
        
        return False