class Solution:
    def evalRPN(self, t: List[str]) -> int:
        a=["*","/","+","-"]
        st=[]
        for i in t:
            if i not in a:
                st.append(int(i))
            else:
                if i=="*":
                    b=st.pop()
                    c=st.pop()
                    st.append(b*c)
                elif i=="/":
                    b=st.pop()
                    c=st.pop()
                    if c//b<0:
                        st.append(ceil(c/b))
                    else:
                        st.append(floor(c/b))
                    print(st[-1])
                elif i=="+":
                    b=st.pop()
                    c=st.pop()
                    st.append(b+c)
                elif i=="-":
                    b=st.pop()
                    c=st.pop()
                    st.append(c-b)
        return st[0]