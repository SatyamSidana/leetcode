class NumArray:
    global a
    a=[]
    def __init__(self, n: List[int]):
        a=[]
        b=0
        for i in range (len(n)):
            b+=n[i]
            a.append(b)
        self.a=a   

    def sumRange(self, l: int, r: int) -> int:
        if l>0:
            return(self.a[r]-self.a[l-1])
        elif l==0:
            return(self.a[r])

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)