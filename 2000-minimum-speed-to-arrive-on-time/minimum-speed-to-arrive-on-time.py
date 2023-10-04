class Solution:
    def minSpeedOnTime(self, d: List[int], h: float) -> int:
        l=1
        hi=1e7
        ans=0
        res=0
        if len(d)-1>=h:
            return -1
        else:
            while(l<=hi):

                mid=(l+hi)//2
                ans=0
                for i in range (len(d)-1):
                    ans+=ceil(d[i]/mid)

                ans+=float(d[len(d)-1]/mid)

                if(mid==1):
                     print(ans)
                     
                #ho-=round(d[-1]/mid,2)
                #print(ho)
                #print(mid)

                if ans<=h:
                    res=mid
                    hi=mid-1
                else:
                    l=mid+1

        return int(res)
                
                
                




            
            

            
        