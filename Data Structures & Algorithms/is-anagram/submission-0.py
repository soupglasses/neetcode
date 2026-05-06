class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = list(s)
        for char in t:
            try:
                chars.remove(char)
            except ValueError:
                return False
        return len(chars) == 0