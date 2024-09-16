import copy

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 1:
            return [["Q"]]
        board = [["."] * n for _ in range(n)]
        def getthehitbox(board, row, col):
            # if col in setblacklist:
            #     return False

            for i in range(0,row):
                boardikub = board[i]
                if boardikub[col] == 'Q':
                    return False
                j = col - (row - i)
                if 0 <= j < n and boardikub[j] == 'Q':
                    return False
                j2 = col + (row - i)
                if 0 <= j2 < n and boardikub[j2] == 'Q':
                    return False
            
            return True

        allkeep = {i: [] for i in range(n + 1)}
        allkeep[0] = [board]
        formatboard = []
        for w in range(1,n+1):
            old_w = w-1
            if old_w != 0:
                allkeep[w-2] = []
                
            allkeep_old = allkeep[old_w]
            for i in range(0,len(allkeep_old)):
                for j in range(0,n):
                    cloneboard = (allkeep_old[i])
                    allkeep[w-1] = []
                    if old_w == 0 or getthehitbox(cloneboard,old_w,j):
                        if w != n:
                            cloneboard = copy.deepcopy(cloneboard)
                        cloneboard[old_w][j] = "Q"
                        if w == n:
                            formatboard.append([''.join(row) for row in cloneboard])
                        else:
                            allkeep[w].append(cloneboard)
        
        allkeep = {}
        board = []
        return formatboard
