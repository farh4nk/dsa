class Solution:
    def equalFrequency(self, word: str) -> bool:
        freq = {}

        for c in word:
            freq[c] = freq.get(c, 0) + 1

        for char in list(freq.keys()):
            freq[char] -= 1

            if freq[char] == 0:
                freq.pop(char)

            counts = set(freq.values())
            if len(counts) == 1:
                return True
                
            freq[char] = freq.get(char, 0) + 1
        return False
