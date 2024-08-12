class Solution:
    def countPairsOfConnectableServers(self, e: List[List[int]], s: int) -> List[int]:
        a = [[] for _ in range(len(e) + 1)]
        for u, v, w in e:
            a[u].append([v, w])
            a[v].append([u, w])
        def dfs(n, p, d, a):
            m = 0
            x = []
            has_child = False

            for i in a[n]:
                if i[0] != p:
                    has_child = True
                    child_count, _ = dfs(i[0], n, i[1] + d, a)
                    if (d + i[1]) % s == 0:
                        child_count += 1
                    m += child_count
                    x.append(child_count)
            
            return (m, x)
        
        ans = []
        for i in range(len(e) + 1):
            if len(a[i]) == 1: 
                ans.append(0)
            else:
                sex = dfs(i, -1, 0, a)
                print(sex)
                su = 0
                mm = sum(sex[1])
                for j in sex[1]:
                    mm -= j
                    su += j * mm
                ans.append(su)
        
        return ans
