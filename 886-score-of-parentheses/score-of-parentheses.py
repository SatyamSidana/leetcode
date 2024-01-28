class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        c=0
        m=0
        st=[]
        for i in s:
            if i=="(":
                m+=1
                if m-1>=len(st):
                    st.append(0)
            elif i==")" and st:
                if m<len(st):
                    st[m-1]+=2*st[m]
                    st.pop()
                else:
                    st[m-1]+=1
                m-=1
            print(st)
            if m==0:
                c+=st[0]
                st=[]
            
        
        return c
        