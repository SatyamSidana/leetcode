class neighborSum:
    def __init__(self, grid: List[List[int]]):
        self.a=grid
        self.b={}
        for i in range(len(self.a)):
            for j in range(len(self.a[0])):
                self.b[self.a[i][j]]=(i,j)
    def adjacentSum(self, v: int) -> int:
        s=self.b[v]
        x,y=s
        c=0
        if x!=0:
            c+=self.a[x-1][y]
        if x!=len(self.a)-1:
            c+=self.a[x+1][y]
        if y!=0:
            c+=self.a[x][y-1]
        if y!=len(self.a[0])-1:
            c+=self.a[x][y+1]
        return c
    def diagonalSum(self, v: int) -> int:
        s=self.b[v]
        x,y=s
        c=0
        i,j=len(self.a)-1,len(self.a[0])-1
        if x!=0 and y!=0:
            c+=self.a[x-1][y-1]
        if x!=0 and y!=j:
            c+=self.a[x-1][y+1]
        if x!=i and y!=0:
            c+=self.a[x+1][y-1]
        if x!=i and y!=j:
            c+=self.a[x+1][y+1]
        return c
        


# Your neighborSum object will be instantiated and called as such:
# obj = neighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)