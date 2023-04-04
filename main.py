ocean_grid = [[x,y] for x in ['1','2','3','4','5','6','7','8','9','10'] for y in ['1','2','3','4','5','6','7','8','9','10']]
target_grid = [[x,y] for x in ['1','2','3','4','5','6','7','8','9','10'] for y in ['1','2','3','4','5','6','7','8','9','10']]
computer_ocean_grid = [[x,y] for x in ['1','2','3','4','5','6','7','8','9','10'] for y in ['1','2','3','4','5','6','7','8','9','10']]
computer_target_grid = [[x,y] for x in ['1','2','3','4','5','6','7','8','9','10'] for y in ['1','2','3','4','5','6','7','8','9','10']]

ship_size = {
  "Carrier": 5,
  "Battleship": 4,
  "Cruiser": 3,
  "Submarine": 2,
  "Destroyer": 1
}

def place_my_ship(type, alignment, row_coord, column_coord):
  h_upper_limit = int(column_coord) + int(ship_size[type])
  v_upper_limit = int(row_coord) + int(ship_size[type])
  if alignment == 'H':
    if int(column_coord) + ship_size[type] > 10:
      return print("Failed placement, outside of board.")
    else:
      for x in ocean_grid:
        if x[0] == row_coord and int(column_coord) <= int(x[1]):
          if len(x) == 3:
            return print("Failed, contains ship.") 
          elif int(x[1]) < h_upper_limit:
              x.append(type)
  elif alignment == 'V':
    if int(row_coord) + ship_size[type] > 10:
      return print("Failed placement, outside of board.")
    for x in ocean_grid:
      if x[1] == column_coord and int(row_coord) <= int(x[0]):
        if len(x) == 3:
          return print("Failed, contains ship.")
        elif int(x[0]) < v_upper_limit:
          x.append(type)
  print(f"{type} placed at [{row_coord},{column_coord}].")

place_my_ship('Carrier', 'H', '1', '1')
place_my_ship('Submarine', 'V', '5', '4')
print(ocean_grid)

def shoot(x_coord, y_coord):
  for x in ocean_grid: #computer_ocean_grid, players for test
    if len(x) == 3:
      if x[0] == x_coord and x[1] == y_coord:
        print("Hit!")
      for x in ocean_grid:
        if x[0] == x_coord and x[1] == y_coord:
          return x.append("Hit.")
      else:
        return print("Miss!")
        #app miss

# shoot('1','1')
# print(target_grid)
      
def output_grid(grid):
  temp_grid = grid.copy()
  #use map on ocean grid to create iterator that yeilds all values for a row,
  #transformed to bluesquare if empty, capital letter for ship name, 
  #fire if hit
  #though map is an iterator, you can print all values as a list()

  #the first thing to do will be to transform the grid to read Blue etc.
  # we can print ten lines at a time and impose grid coords 

  name_key = {
    'Carrier': 'C',
    'Battleship': 'B',
    'Cruiser': 'Cr',
    'Submarine': 'S',
    'Destroyer': 'D'
  }
  
  x_size = (list(map(len, [x for x in grid]))) 

  for x in temp_grid:
    if len(x) == 2:
      x.clear()
      x.append('\u223F')
    elif len(x) == 3:
      if x[2] == 'Carrier':
        x.clear()
        x.append('C')
      elif x[2] == 'Battleship':
        x.clear()
        x.append('B')
      elif x[2] == 'Cruiser':
        x.clear()
        x.append('Cr')
      elif x[2] == 'Submarine':
        x.clear()
        x.append('S')
      elif x[2] == 'Destroyer':
        x.clear()
        x.append('D')
    elif len(x) == 4:
      if x[3] == 'Hit.':
        x.clear()
        x.append('F')

  # for x in grid[::10]:
  #   if x != grid[0]:
  #       x.append('\n')

  

  no_list = ' '.join([''.join(x) for x in grid])

  print(f"""
     1 2 3 4 5 6 7 8 9 10
  1  {no_list[0:19]}
  2  {no_list[20:39]}
  3  {no_list[40:59]}
  4  {no_list[60:79]}
  5  {no_list[80:99]}
  6  {no_list[100:119]}
  7  {no_list[120:139]}
  8  {no_list[140:159]}
  9  {no_list[160:179]}
  10 {no_list[180:199]}
  """)
  
  return print(temp_grid)

  

output_grid(ocean_grid)