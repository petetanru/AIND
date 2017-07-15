from solution import *


def cross(A, B):
  "Cross product of elements in A and elements in B."
  return [i + j for i in A for j in B]

def grid_values(grid):
  """
  Convert grid into a dict of {square: char} with '123456789' for empties.
  Args:
      grid(string) - A grid in string form.
  Returns:
      A grid in dictionary form
          Keys: The boxes, e.g., 'A1'
          Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
  """
  chars = []
  digits = '123456789'
  for c in grid:
    if c in digits:
      chars.append(c)
    if c == '.':
      chars.append(digits)
  assert len(chars) == 81
  return dict(zip(boxes, chars))

def display(values):
  """
  Display the values as a 2-D grid.
  Args:
      values(dict): The sudoku in dictionary form
  """
  width = 1 + max(len(values[s]) for s in boxes)
  line = '+'.join(['-' * (width * 3)] * 3)
  for r in rows:
    print(''.join(values[r + c].center(width) + ('|' if c in '36' else '') for c in cols))
    if r in 'CF': print(line)
  print

rows = 'ABCDEFGHI'
cols = '123456789'

boxes = cross(rows,cols)
row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]

# simply create diagonal units and add it to the unit list.
diag_units = [[''.join(a) for a in zip(rows, cols)], [''.join(a) for a in zip(reversed(rows), cols)]]
unitlist = row_units + column_units + square_units + diag_units

units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)


