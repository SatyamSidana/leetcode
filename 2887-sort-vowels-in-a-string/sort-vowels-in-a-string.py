class Solution:
    def sortVowels(self, s: str) -> str:
        a=[]
        b=[]
        res=s
        c=["a","e","i","o","I","u","U","O","E","A"]
        hw = defaultdict(bool)
        
        for i in c:
            hw[i] = True

        for i in range (len(s)):
            if hw[s[i]]:
                a.append(ord(s[i]))
                b.append(i)
        a.sort()
        for i in range (len(a)):
            j=b.pop()
            res = res[:j] + chr(a.pop()) + res[j + 1:]
        return res    
        