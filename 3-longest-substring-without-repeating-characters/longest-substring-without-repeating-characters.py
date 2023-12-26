class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a={}
        st=0
        e=0
        m=0
        while e<len(s):
            if s[e] in a:
                if a[s[e]]<st:
                    m=max(m,e-st+1)
                else:
                    z=a[s[e]]
                    st=z+1
            else:
            
                
                m=max(m,e-st+1)
            a[s[e]]=e
            e+=1
        return m
            

                


            

        