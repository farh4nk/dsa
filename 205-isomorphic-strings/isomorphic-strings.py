class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map1, map2 = {}, {}
        new_string = ""
        for i in range(len(s)):
            if (s[i] in map1.keys() and map1[s[i]] != t[i]) or (t[i] in map2.keys() and map2[t[i]] != s[i]):
                return False
            map1[s[i]] = t[i]
            map2[t[i]] = s[i]
        for j in range(len(s)):
            new_string += map1[s[j]]
        return new_string == t