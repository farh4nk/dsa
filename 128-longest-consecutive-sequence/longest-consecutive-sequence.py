class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        '''
        convert to set to eliminate duplicates
        for each num:
            if the left neighbor (num-1) doesnt exist, it's the start of a new sequence
            streak becomes 0
            while the right neighbor (num+1) exists, the current sequence is continuing
            streak increments
            at the end of each iteration, update the maximum value
        '''

        s = set(nums)
        maxStreak = 0

        for n in s:
            if n-1 not in s:
                streak = 0
                while n+streak in s:
                    streak += 1
                maxStreak = max(maxStreak, streak)

        return maxStreak