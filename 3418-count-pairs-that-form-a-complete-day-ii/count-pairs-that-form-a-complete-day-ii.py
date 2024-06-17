class Solution:
    def countCompleteDayPairs(self, h: List[int]) -> int:
        a=[0]*25
        c=0
        for i in h:
            if i%24==0:
                c+=a[0]
                a[0]+=1
            else:
                c+=a[24-(i%24)]
                print(a[24-(i%24)],24-(i%24))
                a[(i%24)]+=1
        return c
