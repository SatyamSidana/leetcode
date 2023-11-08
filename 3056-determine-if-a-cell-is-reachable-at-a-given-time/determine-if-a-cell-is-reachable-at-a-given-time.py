class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        #if t>(fy-sx+fx-sy):
            #return False
        if fx==sx and fy==sy and t==1:
            return False
        elif t>=max(abs(fy-sy),abs(fx-sx)):
            return True       
        else:
            return False