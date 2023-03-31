## next step is to make code more elegant then classful
# victory condition function
# sunk ship function

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

def place_my_ship(type, alignment, x_coord, y_coord):
  h_upper_limit = int(y_coord) + int(ship_size[type])
  v_upper_limit = int(x_coord) + int(ship_size[type])
  if alignment == 'H':
    if int(y_coord) + ship_size[type] > 11:
      return print("Failed placement, outside of board")
    for x in ocean_grid:
      if x[0] == x_coord and int(y_coord) <= int(x[1]) < 11:
        if len(x) == 3:
          return print("Failed, contains ship.") 
        elif int(x[1]) < h_upper_limit:
            x.append(type)
  elif alignment == 'V':
    if int(x_coord) + ship_size[type] > 11:
      return print("Failed placement, outside of board.")
    for x in ocean_grid:
      if x[1] == y_coord and int(x_coord) <= int(x[0]) < 11:
        if len(x) == 3:
          return print("Failed, contains ship.")
        elif int(x[0]) < v_upper_limit:
          x.append(type)
  print(f"{type} placed at [{x_coord},{y_coord}].")

place_my_ship('Carrier', 'H', '1', '1')
place_my_ship('Battleship', 'H', '9', '4')
place_my_ship('Cruiser', 'V', '5', '3')
place_my_ship('Submarine', 'V', '3', '1')
place_my_ship('Destroyer', 'H', '10', '10')
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

shoot('1','1')
print(target_grid)
      
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
      x.append('Blue')
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
    
  
  return print(temp_grid)

  

output_grid(ocean_grid)