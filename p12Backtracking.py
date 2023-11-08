'''
https://www.educative.io/courses/grokking-coding-interview-patterns-python/g7qQw2kqN6D
Solution: N-Queens

Given a chessboard of sizen×n, determine how many ways n queens can be placed on the board, such that no two queens attack each other.

A queen can move horizontally, vertically, and diagonally on a chessboard. One queen can be attacked by another queen if both share the same row, column, or diagonal.

Time complexity
The time complexity of this solution is O(n^n), where n is the dimension of the chessboard.

Space complexity
The space complexity of this solution is O(n), where n is the dimension of the chessboard.

'''
# SOLUTION 2
# This solution uses stack to store the solution.
# Stack will hold only the column values and one solution
# will be stored in the stack at a time.

def is_valid_move(proposed_row, proposed_col, solution):
  # we need to check with all queens
  # in current solution
  for i in range(0, proposed_row):
    old_row = i
    old_col = solution[i]

    diagonal_offset = proposed_row - old_row
    if (old_col == proposed_col or
      old_col == proposed_col - diagonal_offset or
        old_col == proposed_col + diagonal_offset):
      return False

  return True


def solve_n_queens(n):
  results = []
  solution = [-1] * n
  sol_stack = []

  row = 0
  col = 0

  while row < n:
    # For the current state of the solution, check if a queen can be placed in any
    # column of this row
    while col < n:
      if is_valid_move(row, col, solution):
        # If this is a safe position for a queen (a valid move), save 
        # it to the current solution on the stack...
        sol_stack.append(col)
        solution[row] = col
        row = row + 1
        col = 0
        # ... and move on to checking the next row (breaking out of the inner loop)
        break
      col = col + 1

    # If we have checked all the columns
    if col == n:
      # If we are working on a solution
      if sol_stack:
        # Backtracking, as current row does not offer a safe spot given the previous move
        # So, get set up to check the previous row with the next column
        col = sol_stack[-1] + 1
        sol_stack.pop()
        row = row - 1
      else:
        # If we have backtracked all the way and found this to be a dead-end,
        # break out of the inner loop
        break  # no more solutions exist
      
    # If we have found a safe spot for a queen in each of the rows
    if row == n:
      # add the solution into results
      results.append(solution)

      # backtrack to find the next solution
      row = row - 1
      col = sol_stack[-1] + 1
      sol_stack.pop()

  return len(results)

def main():
  n = [4, 5, 6, 7, 8]
  for i in range(len(n)):
      res = solve_n_queens(n[i])
      print(i+1, ".\tTotal solutions count for ", n[i], " queens on the chessboard (", n[i], "x", n[i], "): ", res, sep ="")
      print("-"*100, "\n", sep = "")


if __name__ == '__main__':
  main()
