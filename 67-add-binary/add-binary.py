class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c=""
        r=0
        i=len(a)-1
        j=len(b)-1
        while i>=0 and j>=0:
            if int(a[i])+int(b[j])+r>1:
                c+=(str(int(a[i])+int(b[j])+r-2))
                r=1
            else:
                c+=str(int(a[i])+int(b[j])+r)
                r=0
            i-=1
            j-=1
        while i>=0:
            if int(a[i])+r>1:
                c+=(str(int(a[i])+r-2))
                r=1
            else:
                c+=str(int(a[i])+r)
                r=0
            i-=1
        while j>=0:
            if int(b[j])+r>1:
                c+=(str(int(b[j])+r-2))
                r=1
            else:
                c+=str(+int(b[j])+r)
                r=0
            j-=1
        if r:
            c+="1"
        return c[::-1]

        