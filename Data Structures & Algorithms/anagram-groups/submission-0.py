from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = defaultdict(list)
        for elem in strs:
            key = tuple(sorted(elem))
            answer[key].append(elem)
        return list(answer.values())
