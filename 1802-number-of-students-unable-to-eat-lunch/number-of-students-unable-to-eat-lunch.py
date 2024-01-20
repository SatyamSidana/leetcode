class Solution:
    def countStudents(self, s: List[int], f: List[int]) -> int:
        c=0
        while len(f)>0:
            if s[0]==f[0]:
                s.pop(0)
                f.pop(0)
                c=0
            else:
                s.append(s[0])
                s.pop(0)
                c+=1
            if c==len(s):
                break
        return len(s)

        


        