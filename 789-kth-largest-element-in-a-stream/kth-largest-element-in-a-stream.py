class KthLargest:

    def __init__(self, k: int, n: List[int]):
        n.sort()
        self.a=n
        self.i=-k

    def add(self, v: int) -> int:
        l=0
        h=len(self.a)-1
        while l<=h:
            mid=(l+h)//2
            if self.a[mid]>v:
                h=mid-1
            else:
                l=mid+1
        self.a=self.a[:l]+[v]+self.a[l:]
        return self.a[self.i]
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)