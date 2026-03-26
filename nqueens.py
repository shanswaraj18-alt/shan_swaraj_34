class solution:
    def solve(self,col,board,ans,leftrow,upperdiagonl,lowerdiagonl,n):
        if col ==n:
            ans.append(board[:])
            return
        for row in range(n):
            if leftrow[row]==0 and lowerdiagonl[row+col]==0 and upperdiagonl[n-1+col-row]==0 :
                board[row]= board[row][:col]+"Q"+board[row][col +1:]
                leftrow[row]=1
                lowerdiagonl[row + col]=1
                upperdiagonl[n-1+col-row]=1
                self.solve(col+1,board,ans,leftrow,upperdiagonl,lowerdiagonl,n)
                board[row]= board[row][:col]+"."+board[row][col+1:]
                leftrow[row]=0
                lowerdiagonl[row +col]=0
                upperdiagonl[n-1+col-row]=0
    def solvenqueens(self,n:int):
        ans =[]
        board=["."*n for _ in range(n)]
        leftrow = [0]*n
        upperdiagonl = [0]*(2*n-1)
        lowerdiagonl = [0]*(2*n-1)
        self.solve(0,board,ans,leftrow,upperdiagonl,lowerdiagonl,n)
        return ans
object = solution()
print(object.solvenqueens(4))            


            
                