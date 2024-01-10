class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        m={}
        a=[]
        s=[]
        s.append((t[0],0))
        for i in range (1,len(t)):
            while s and t[i]>s[-1][0]:
                if s[-1][0] in m:
                    m[s[-1][0]][s[-1][1]]=i-s[-1][1]
                else:
                    m[s[-1][0]]={}
                    m[s[-1][0]][s[-1][1]]=i-s[-1][1]
                s.pop()
            s.append((t[i],i))
        for i in range (len(s)):
            if s[i][0] in m:
                m[s[i][0]][s[i][1]]=0
            else:
                m[s[i][0]]={}
                m[s[i][0]][s[i][1]]=0
                
        print(m)
        for i in range (len(t)):
            a.append(m[t[i]][i])
        print(m)
        return a

                

        