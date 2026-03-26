class solution():

    def findpathhelper(self,
        i:int ,
        j: int,
        a :list[list[int]],
        n : int,
        ans: list[str],
        move: str,
        vis : list[list[int]]
     ):
        if i == n-1 and j== n-1:
         ans.append(move)
         return
    #downwrd movement
        if i+1<n and vis[i+1][j] == 0 and a[i+1][j]==1:
            vis[i][j]=1
            self.findpathhelper(i+1,j,a,n,ans,move + "D",vis)
            vis[i][j]=0
    #left movement
        if j-1>=0 and vis[i][j-1]==0 and a[i][j-1]==1:
           vis[i][j]=1
           self.findpathhelper(i,j-1,a,n,ans,move+"L",vis)
           vis[i][j]=0
    #upward movement 
        if i-1>=0 and vis[i-1][j] == 0 and a[i-1][j]==1:
           vis[i][j]=1
           self.findpathhelper(i-1,j,a,n,ans,move + "U",vis)
           vis[i][j]=0
    # right movement
        if j+1<n and vis[i][j+1] == 0 and a[i][j+1]==1:
            vis[i][j]=1
            self.findpathhelper(i,j+1,a,n,ans,move + "R",vis)
            vis[i][j]=0
    def ratmaze(self,matrix :list[list[int]]):
        n = len(matrix)
        ans = []
        vis = [[0 for _ in range(n)] for _ in range(n)]
        if matrix[0][0]==1:
            self.findpathhelper(0,0,matrix,n,ans,"",vis)
        return ans 
obj = solution()
print(obj.ratmaze([[1,0,0,0],[1,1,0,0],[1,1,0,0],[0,1,1,1]]))               
       

