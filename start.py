import sys
from lib.data import Data

#print(int(sys.argv[1]))

try:
    size = sys.argv[1]
    # Generate Images
    
    if isinstance(int(size), int) != True:
        raise Exception()
    if int(size) == 0:
        size = 128
    print("Generating Image size (" + size + "x" + size + ")px")
    size = int(size)
    Data().gen(size)
except :
    print("Please pass correct image size")
