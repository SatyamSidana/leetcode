class Solution:
    def maxChunksToSorted(self, a: List[int]) -> int:
        st=[]
        c=0
        l=0
        for i in range (len(a)):
            st.append(a[i])
            st.sort()
            if st[-1]==i:
                c+=1
                st=[]
        return c


        