class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        a=defaultdict(int)
        e=0
        st=0
        m=0
        while e<len(s):
            a[s[e]]+=1
            if a[s[e]]>2:
                while s[st]!=s[e]:
                    a[s[st]]-=1
                    st+=1
                a[s[st]]-=1
                st+=1
            m=max(m,e-st+1)
            e+=1
        return m