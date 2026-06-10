class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for s in strs:
            sorte="".join(sorted(s))
            res[sorte].append(s)
        return list(res.values())
