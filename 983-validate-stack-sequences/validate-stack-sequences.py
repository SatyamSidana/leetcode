class Solution:
    def validateStackSequences(self, p: List[int], po: List[int]) -> bool:
        a={}
        st=[]
        j=0
        for i in range (len(po)):
            if po[i] in a:
                print(po[i]) 
                if st[-1]!=po[i]:
                    return False
                else:
                    st.pop()
            else:
                while j<len(p):
                    if p[j]==po[i]:
                        j+=1
                        break
                    else:
                        st.append(p[j])
                        a[p[j]]=0
                    j+=1
            print(st,a)
        return True
        