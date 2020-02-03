# This Program caluclates howmany tiles you will need
#  When tiling a wall or floor in metres squared
length = float(input ("Enter Room Length: "))
width = float(input ("Enter Room Width: "))
#length = 4.3
#1width = 2.2
Area = length * width

needed = Area * 1.05
print ("You need ", needed ,"Tiles in metres squared")


