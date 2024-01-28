class Solution:
    def find132pattern(self, n: List[int]) -> bool:
        st=[]
        st.append(n[-1])
        i=len(n)-2
        m=-10**9
        while i>=0:
            if n[i]<m:
                return True
            if n[i]<st[-1]:
                st.append(n[i])
            elif n[i]>st[-1]:
                while st and n[i]>st[-1]:
                    m=st.pop()
                st.append(n[i])
            i-=1    
        return False
        