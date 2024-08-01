class Solution:
    

    def restoreIpAddresses(self, s: str) -> List[str]:
        def valid(x):
            return x == str(int(x)) and int(x) <= 255
        n = len(s)
        ans = []
        for i in range(1, n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    a, b, c, d = s[:i], s[i:j], s[j:k], s[k:]
                    if valid(a) and valid(b) and valid(c) and valid(d):
                        ans.append(a+"."+b+"."+c+"."+d)
        return ans
        
            
