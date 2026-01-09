class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        answer = [0] * len(score)
        indices = {}
        for i, n in enumerate(score):
            indices[n] = i
        score.sort(reverse=True)
        for i, s in enumerate(score):
            rank = i + 1
            if rank == 1:
                ans = "Gold Medal"
            elif rank == 2:
                ans = "Silver Medal"
            elif rank == 3:
                ans = "Bronze Medal"
            else:
                ans = str(rank) 
            answer[indices[s]] = ans
        return answer
            

