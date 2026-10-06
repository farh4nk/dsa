class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        sliding window
        start l = 0
        iterate through s with r
        for each char at r
        if its in the window
        remove the char at l from window
        increment l
        otherwise add it to the window
        update the max at each iteration
        '''

        res = 0
        window = set()
        l = 0
        for r in range(len(s)):
            curr = s[r]
            while curr in window:
                window.remove(s[l])
                l += 1
            window.add(curr)

            res = max(res, (r - l + 1))

        return res

            


