# Validate a minesweeper interior block
# block_data is a two dimensional array containing the data from a 3 x 3 grid of squares
# We are assuming that we are only checking interior blocks for now
# Return value should be a string that says either Valid or Invalid (with some hints as to why it's invlaid)
try:
  def validate( block_data ):
    # Check whether the centre block is a bomb, a number, or an invalid input
    # Skip bombs, send an error on invalid input, verify numbers
    bomb_count = 0
    result=""
    for i in range(3):
      for j in range(3):
        if block_data [i][j]==-1:
          bomb_count = bomb_count + 1
    if block_data [1][1] == -1:
      result= "bomb"
    if block_data[1][1] == bomb_count:
      result="valid"
    if block_data[1][1] != bomb_count:
      result= "invalid, the interior square is not equal to the number of bombs."
    return result



  grid = [
    [-1,-1,0],
    [1,a,0],
    [0,0,-1]
  ]
  print (validate(grid))

except:
  print("Error")
  print("Not all of the blocks are numbers. Please ensure every block is a number.")

