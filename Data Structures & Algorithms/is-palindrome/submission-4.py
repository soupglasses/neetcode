import re

class Solution:
    RE = re.compile(r"[^a-z0-9]")

    def isPalindrome(self, s: str) -> bool:
        s = self.RE.sub("", s.lower())
        if len(s) <= 1:
            return True
        l, r = 0, len(s)-1
        while l <= len(s)//2:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True