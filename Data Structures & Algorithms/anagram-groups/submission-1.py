from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = defaultdict(list)
        for elem in strs:
            counts = [0] * 26 # english lowercase (a-z)
            for char in elem:
                counts[ord(char) - ord('a')] += 1
            answer[tuple(counts)].append(elem)
        return list(answer.values())