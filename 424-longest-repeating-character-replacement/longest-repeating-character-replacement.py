class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        sliding window
        add to frequency hashmap while iterating through s
        number of replacements needed in a window is
        size of window - freq of most frequent letter
        if insufficient replacements
        move up l and decrement freq at l
        otherwise update the max
        '''

        res = 0
        freq = {}
        l = 0
        for r in range(len(s)):
            curr = s[r]
            freq[curr] = freq.get(curr, 0) + 1

            max_repl = (r - l + 1) - max(freq.values())
            if max_repl <= k:
                res = max(res, (r - l + 1))
            else:
                freq[s[l]] -= 1
                l += 1
        return res