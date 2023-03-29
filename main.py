ocean_grid = [[x,y] for x in ['1','2','3','4','5','6','7','8','9','10'] for y in ['1','2','3','4','5','6','7','8','9','10']]

#use x + y and list A-J for normal

target_grid = [[x,y] for x in ['A','B','C','D','E','F','G','H','I','J'] for y in ['1','2','3','4','5','6','7','8','9','10']]

print(ocean_grid)

# C = Carrier, B = Battleship, Cr = Crusier, S = Submarine, D = Destroyer 

# row, column
#size, anchor point(fore of ship), will be L->R and T->B horizontal or vertical
#function that checks suitability for placement?

ship_size = {
  "Carrier": 5,
  "Battleship": 4,
  "Cruiser": 3,
  "Submarine": 2,
  "Destroyer": 1
}

def place_my_ship(type, alignment, x_coord, y_coord):
  upper_limit = int(y_coord) + int(ship_size[type])
  ship_keys = [x for x in ship_size.keys()]
  print(ship_keys)
  if alignment == 'H':
    if int(y_coord) + ship_size[type] > 10: #10th row?
      print("Failed placement.")
    for x in ocean_grid:
      if x[0] == x_coord:
        if len(x) == 3: #fail if even only one contains ship
          return print("Failed, contains ship.")
        elif int(x[1]) < upper_limit: #serves as counter
          x.append(type)
          #fine h
          #call input Confirm placement
  elif alignment == 'V':
    if int(y_coord) + ship_size[type] > 10:
      print("Failed placement.")
    for x in ocean_grid:
      if x[1] == y_coord:
        #x coord will need a range or will append to only a single row 
        if len(x) == 3:
          return print("Failed, contains ship.")
        elif int(x[0]) < upper_limit:
          x.append(type)
  return print(f"{type} placed at [{x_coord},{y_coord}].")
  

                   #next problem is to stop operation completely if longer ship overrides shorter 
          
      #if the 0 index is equal to coords[0]
      #and 1 index to range coords[1] + ship_size[type]
      #upper_limit = coords[1] + (ship_size[type] -1)
      #if x[1] < upper_limit
      #x.append Type at index 2 


      
#  if horizontal alignment 
#      if number + size > 10,
#        placement failed, does not fit
#      if number + size <= 10,
#        iterate over coords for len of ship, converting them to ship letter 
#      check is not int, if not return you can't place over another ship
#  if vertical alignment
#      if number + size > 10,
#        placement failed, does not fit
#      if number + size <= 10,
#        iterate over coords for len of ship, converting them to ship letter ... not ssame as horizontal, need to move to next row same column e.g. 1,1 next would be 2,1 .. check if not int if not can't place over another ship!
# then update the ocean grid to reflect placement

# def placement_information():
#   for t in ['Carrier', 'Battleship', 'Cruiser', 'Submarine', 'Destroyer']:
#     a = input(f"Select alignment for your {t}: ")
#     c = input(f"Select anchor co-ords for your {t}: ")
#     place_my_ship(t, a, c)

place_my_ship('Cruiser', 'H', '1', '1')
print(ocean_grid)
place_my_ship('Destroyer', 'V', '5', '3')
print(ocean_grid)
