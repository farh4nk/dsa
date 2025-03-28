# 217. Encode and Decode Strings
# Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.
# Please implement encode and decode
# Example 1:
# Input: ["neet","code","love","you"]
# Output:["neet","code","love","you"]
# Example 2:
# Input: ["we","say",":","yes"]
# Output: ["we","say",":","yes"]

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += (str(len(s)) + "#" + s) # length followed by # indicates a word
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        p = 0
        while p < len(s):
            i = p
            while s[i] != "#":
                i += 1
            l = int(s[p:i]) # slice needed b/c following string may be more than 9 chars long
            res.append(s[i + 1: i + 1 + l])
            p =i +l + 1 
        return res
