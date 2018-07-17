# Print concentric rectangular pattern in a 2d matrix. 
# Let us show you some examples to clarify what we mean.

# Example 1:

# Input: A = 4.
# Output:

# 4 4 4 4 4 4 4 
# 4 3 3 3 3 3 4 
# 4 3 2 2 2 3 4 
# 4 3 2 1 2 3 4 
# 4 3 2 2 2 3 4 
# 4 3 3 3 3 3 4 
# 4 4 4 4 4 4 4 

def pretty_print(size):
  if size < 1:
    return []
  if size == 1:
    return [[1]]
  
  grid_size = (size * 2) - 1
  grid = [[0 for x in range(grid_size)] for x in range(grid_size)]

  top_left = [0,0]
  top_right = [0, len(grid)-1]
  bottom_right = [len(grid)-1, 0]
  count = size
  length = grid_size

  while (count > 1):
    for i in range(length):
      # populate horizontally
      grid[top_left[0]][top_left[1]+i] = count 
      grid[bottom_right[0]][bottom_right[1]+i] = count
      # populate vertically
      grid[top_left[0]+i][top_left[1]] = count
      grid[top_right[0]+i][top_right[1]] = count
    count -= 1
    top_left[0] += 1
    top_left[1] += 1
    top_right[0] += 1 
    top_right[1] -= 1 
    bottom_right[0] -= 1
    bottom_right[1] += 1
    length -= 2
  # populate center of the grid 
  grid[top_left[0]][top_left[1]] = count
  return grid

print(pretty_print(4))
