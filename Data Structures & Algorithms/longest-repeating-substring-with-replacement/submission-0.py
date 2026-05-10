from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right, max_len = 0, 0, 0
        seen = Counter()
        while right < len(s):
            seen[s[right]] += 1
            while (seen.total() - max(seen.values())) > k:
                seen[s[left]] -= 1
                if seen[s[left]] == 0:
                    del seen[s[left]]
                left += 1
            max_len = max(max_len, right - left + 1)
            right += 1

        return max_len