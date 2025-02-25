from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_valid(col, row, board, n):
            tcol, trow = col, row
            # Check upper diagonal on left side
            while col >= 0 and row >= 0:
                if board[row][col] == 'Q':
                    return False
                row -= 1
                col -= 1
            col, row = tcol, trow
            # Check left side
            while col >= 0:
                if board[row][col] == 'Q':
                    return False
                col -= 1
            col, row = tcol, trow
            # Check lower diagonal on left side
            while row < n and col >= 0:
                if board[row][col] == 'Q':
                    return False
                col -= 1
                row += 1
            return True
        
        def solve(col, board, n, result):
            if col == n:
                result.append(["".join(row) for row in board])
                return
            for row in range(n):
                if is_valid(col, row, board, n):
                    board[row][col] = 'Q'
                    solve(col + 1, board, n, result)
                    board[row][col] = '.'
        
        board = [['.' for _ in range(n)] for _ in range(n)]
        result = []
        solve(0, board, n, result)
        return result

# Example usage:
solution = Solution()
n = 4
results = solution.solveNQueens(n)
for result in results:
    for row in result:
        print(row)
    print()

"""
solveNQueens Method:
This method takes an integer n as input and returns a list of solutions for the N-Queens problem, where n is the size of the chessboard (n x n).
It defines two nested functions within the solveNQueens method: is_valid and solve.
is_valid Function:
This function checks if placing a queen at a specific position (col, row) on the board is valid or not.
It takes four parameters: col (column index), row (row index), board (the current state of the chessboard), and n (board size).
The function first stores the original values of col and row in tcol and trow for later use.
It checks three conditions to determine if placing a queen at (col, row) is valid:
Upper diagonal on the left side: Checks if there is any queen on the upper diagonal (left direction) of the current position.
Left side: Checks if there is any queen on the same row to the left of the current position.
Lower diagonal on the left side: Checks if there is any queen on the lower diagonal (left direction) of the current position.
If any of these conditions is violated, the function returns False, indicating that placing a queen at (col, row) is not valid. Otherwise, it returns True.
solve Function:
This function is a recursive backtracking algorithm to solve the N-Queens problem.
It takes four parameters: col (current column), board (the current state of the chessboard), n (board size), and result (the list to store valid solutions).
If col reaches n, it means all queens are successfully placed, so it appends the current state of the board to result.
Otherwise, it tries placing a queen in each row of the current column (col) and recursively calls itself to explore further possibilities.
If placing a queen at a specific position is valid (is_valid returns True), it places the queen ('Q') on the board, calls solve for the next column (col + 1), and then removes the queen ('.') from that position to backtrack and explore other possibilities.
Example Usage:
Creates an instance of the Solution class.
Sets n = 4 for a 4x4 chessboard.
Calls solveNQueens to solve the N-Queens problem for a 4x4 board and stores the solutions in results.
Prints each solution, where each solution is represented as a list of strings (each string represents a row on the board).
"""
