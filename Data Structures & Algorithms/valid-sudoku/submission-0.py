class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Checks rows
        for row in board:
            s = set()
            for col in row:
                if col != ".":
                    if col in s:
                        return False
                    s.add(col)

        # Checks columns
        for col in range(len(board[0])):
            s = set()
            for row in range(len(board)):
                if board[row][col] != ".":
                    if board[row][col] in s:
                        return False
                    s.add(board[row][col])

        # Checks boxes
        boxes = []
        for i in range(0,9):
            row_start = (i // 3) * 3
            col_start = (i % 3) * 3
            s = set()
            for j in range(0,3):
                for k in range(0,3):
                    r_offset = row_start + j
                    c_offset = col_start + k
                    if board[r_offset][c_offset] != ".":
                        if board[r_offset][c_offset] in s:
                            return False
                        s.add(board[r_offset][c_offset])
            print(s)

        return True 
