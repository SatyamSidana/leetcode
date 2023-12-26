class Solution:
    def missingNumber(self, n: List[int]) -> int:
        n.sort()
        for i in range (len(n)):
            if n[i]!=i:
                return i
        return len(n)

        