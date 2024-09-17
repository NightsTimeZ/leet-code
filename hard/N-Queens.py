import pickle
# best ;> very simple
class Solution:
    def addtheredzone(self,board,row,colum,n):
        for i in range(0,n):
            board[row][i] = "X"
            board[i][colum] = "X"
            j = colum - (row - i)
            if 0 <= j < n:
                board[i][j] = "X"
            j2 = colum + (row - i)
            if 0 <= j2 < n:
                board[i][j2] = "X"
    def deepcopy(self,board):
        return pickle.loads(pickle.dumps(board))
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 1:
            return [["Q"]]
        
        board = [["."]*n for _ in range(n)]
        res = []
        def backtrack_maybe(board,row):
            if row == n:
                res.append([''.join('.' if cell == 'X' else cell for cell in row) for row in board])
                return
            for col in range(0,n):
                if board[row][col] == ".":
                    cloneboard = board
                    if row != n-1:
                        cloneboard = self.deepcopy(cloneboard)
                        self.addtheredzone(cloneboard,row,col,n)
                    cloneboard[row][col] = "Q"
                    backtrack_maybe(cloneboard,row+1)
        backtrack_maybe(board,0)
        return res
