class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        seen = list()
        max_len = 0
        while right < len(s):
            char = s[right]
            if char not in seen:
                seen.append(char)
                right += 1
            else:
                i = seen.index(char)
                del seen[0:i+1]
                left += i
            max_len = max(len(seen), max_len)
        return max_len