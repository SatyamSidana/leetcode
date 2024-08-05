class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        prefix_b = [0]
        suffix_a = [0] * n
        for i in range(1, n):
            if s[i - 1] == 'b':
                prefix_b.append(prefix_b[-1] + 1)
            else:
                prefix_b.append(prefix_b[-1])
        for i in range(n - 2, -1, -1):
            if s[i + 1] == 'a':
                suffix_a[i] = suffix_a[i + 1] + 1
            else:
                suffix_a[i] = suffix_a[i + 1]
    
        res = inf
        for pivot in range(n):
            res = min(res, prefix_b[pivot] + suffix_a[pivot])
        return res