class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            seen = dict()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in seen.keys():
                    return False
                else:
                    seen[board[i][j]] = True
            
        for i in range(9):
            seen = dict()
            for j in range(9):
                if board[j][i] == ".":
                    continue
                if board[j][i] in seen.keys():
                    return False
                else:
                    seen[board[j][i]] = True

        for square in range(9):
            seen = dict()
            for i in range(3):    
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen.keys():
                        return False
                    else:
                        seen[board[row][col]] = True

        return True