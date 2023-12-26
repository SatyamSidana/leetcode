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
                    print(st,e)
                else:
                    z=a[s[e]]
                    print("z",s[e],z)
                    st=z+1
                a[s[e]]=e
                e+=1
            else:
                a[s[e]]=e
                print(a)
                print(st,e)
                
                m=max(m,e-st+1)
                e+=1
        return m
            

                


            

        