import copy
## bull shit n Queens with  brute force
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 1:
            return [["Q"]]
        board = [["."] * n for _ in range(n)]
        def getthehitbox(board, row, col):
            n = len(board)
            
            for i in range(row):
                if board[i][col] == 'Q':
                    return False
                j = col - (row - i)
                if 0 <= j < n and board[i][j] == 'Q':
                    return False
                j2 = col + (row - i)
                if 0 <= j2 < n and board[i][j2] == 'Q':
                    return False
            
            return True

        allkeep = {i: [] for i in range(n + 1)}
        allkeep[0] = [copy.deepcopy(board)]
        for w in range(1,n+1):
            for i in range(0,len(allkeep[w-1])):
                for j in range(0,n):
                    cloneboard = copy.deepcopy(allkeep[w-1][i])
                    if getthehitbox(cloneboard,w-1,j):
                        cloneboard[w-1][j] = "Q"
                        allkeep[w].append(cloneboard)

        def format_boards(boards):
            formatted_boards = []
            for board in boards:
                formatted_board = [''.join(row) for row in board]
                formatted_boards.append(formatted_board)
            return formatted_boards
        return (format_boards(allkeep[n]))
