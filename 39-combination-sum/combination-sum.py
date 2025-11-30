class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, combo):
            total = sum(combo)
            if total == target:
                res.append(combo.copy())
                return
            if i >= len(candidates) or total > target:
                return

            combo.append(candidates[i])
            backtrack(i, combo)

            combo.pop()
            backtrack(i+1, combo)

        backtrack(0, [])

        return res

