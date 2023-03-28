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


def place_my_ship(type, alignment, coords):
  upper_limit = int(coords[1]) + int(ship_size[type])
  if alignment == 'H':
    if int(coords[1:]) + ship_size[type] > 10:
      print("Failed placement.")
    #now account for coords[2] being a type
    else:
      for x in ocean_grid:
        if x[0] == coords[0]: #correct row
          if int(x[1]) < upper_limit:
            x.append(type)
          
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

place_my_ship('Cruiser', 'H', '11')
print(ocean_grid)