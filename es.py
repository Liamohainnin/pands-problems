# Liam O Hainnin
import itertools
fname = input("Enter the name of the file:")
Searchchar = {'e','E'}
with open(fname) as f:
 print(sum(1 for char in  itertools.chain.from_iterable(f) if char in Searchchar))



