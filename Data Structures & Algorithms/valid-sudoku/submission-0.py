class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])

        # check each row
        for r in range(rows):
            seen = set()
            for c in range(cols):
                if board[r][c] != ".": 
                    if board[r][c] not in seen:
                        seen.add(board[r][c])
                    else:
                        return False  

        # check each col
        for c in range(cols):
            seen = set()
            for r in range(rows):
                if board[r][c] != ".": 
                    if board[r][c] not in seen:
                        seen.add(board[r][c])
                    else:
                        return False  

        # check each grid
        for square in range(9):
            seen = set()
            for r in range(3):
                for c in range(3):
                    row = (square // 3) * 3 + r
                    col = (square % 3) * 3 + c
                    if board[row][col] != ".":
                        if board[row][col] not in seen:
                            seen.add(board[row][col])
                        else:
                            return False

        return True