from collections import defaultdict as dd
class Solution:
    def getFreq(self, s):
        freq = dd(lambda: 0)
        for c in s:
            freq[c] += 1
        return freq
    def firstUniqChar(self, s: str) -> int:
        freq = self.getFreq(s)
        for c in freq:
            if freq[c] == 1:
                return s.index(c)
        return -1