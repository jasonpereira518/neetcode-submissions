from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = dict(Counter(s))
        seen2 = dict(Counter(t))

        return seen == seen2