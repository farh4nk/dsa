class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        sorts = defaultdict(list)

        for s in strs:
            sorts[''.join(sorted(s))].append(s)
        return list(sorts.values())