ocean_grid = [[x,y] for x in ['1','2','3','4','5','6','7','8','9','10'] for y in ['1','2','3','4','5','6','7','8','9','10']]

#use x + y and list A-J for normal

target_grid = [[x,y] for x in ['A','B','C','D','E','F','G','H','I','J'] for y in ['1','2','3','4','5','6','7','8','9','10']]

print(ocean_grid)

# C = Carrier, B = Battleship, Cr = Crusier, S = Submarine, D = Destroyer 

# row, column
#size, anchor point(fore of ship), will be L->R and T->B horizontal or vertical
#function that checks suitability for placement?

place = input("Place you ship T/A/C e.g. CH11 ")

ship_size = {
  "Carrier": 5,
  "Battleship": 4,
  "Cruiser": 3,
  "Submarine": 2,
  "Destroyer": 1
}


def place_my_ship(place):
  #need to input three separate, Type Align and Coords
  #as splicing doesn't work with double digit coords
  type = place[:-3]
  alignment = place[-3]
  coords = place[-2:]
  print(type, alignment, coords)
  print(coords[1])
  print(ship_size[type])
  if alignment == 'H':
    if int(coords[1]) + ship_size[type] > 10:
      print("Failed placement.")
    else:
      print("Placement success.")
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

place_my_ship(place)