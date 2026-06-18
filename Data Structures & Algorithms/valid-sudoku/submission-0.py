class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        Understanding: 
        - in this board.length == 9
        - board[i].length == 9
        - board[i][j] is a digit 1-9 or '.'
        - How do we iterate through the board 
            with row, column and sub box in mind
            hash or dict sub box to keep a list of numbers, (thats how we check for repeats), happens every 3 rows
        - we only go through rows unless a digit is in board[i][j]
        - if board[i][j] is not empty, check column to see if no repeats of digit, we dont need to worry about rows above
            because they would have already been checked

        Planning; 
        - check row board[i][j], if board[i][j] != '.', check column
            if board[i][j] != '.' and unique in column keep checking in row
            if board[i][j] repeats return false 
        - if board[i][j] == (other column [i][j]) return False
        - add to dict board[i][j], until board[i+2][j+2] check if dict has repeat if yes return false
        '''

        for row in range(9):
            seen = set()
            for i in range(9):
                if board[row][i] == '.':
                    continue
                if board[row][i] in seen:
                    return False
                seen.add(board[row][i])

        for col in range(9):
            seen = set()
            for i in range(9):
                if board[i][col] == '.':
                    continue
                if board[i][col] in seen: 
                    return False
                seen.add(board[i][col])

        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square%3) * 3 + j
                    if board[row][col] == '.':
                        continue
                    if board[row][col] in seen: 
                        return False
                    seen.add(board[row][col])
        
        return True
