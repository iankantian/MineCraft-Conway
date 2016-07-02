#Minecraft Conway's Game of Life
#Blocks live, die, or are born to the cruel rules of nature
#But along the way, there is beauty!
from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

xo = -94
yo = 85
zo = 76

blockType = 5; # classic oak plank

# the side length of the array,
# should be able to have any aspect ratio, but I don't understand getBlocks
# well enough to fix this.  It's not returning as I excpect unless it's a
# square array
width = 50
depth = 50

# manually wrote a non square array to test logic below, it works just fine.
#blocks = [0,0,0,0,41,41,41,41,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]

while 1: # Infinite loop!!!!!!!5
    onSwitch = mc.getBlock(-94, 83, 78);
    if onSwitch: # if it's there, the code runs!
        # get the width and height worth of blocks
        blocks = mc.getBlocks(xo, yo, zo, xo+width-1, yo, zo+depth-1)
        
        # split up the result into depth-number of rows in an array of width-number columns
        twoDBlocks = [] # empty list
        test = 0 # a variable to increment jus' by one
        for z in range(depth):
            twoDBlocks.append( blocks[test : test + width] )
            test += width

        # find the number of neighbors! 
        for z in range(1, depth-1): # each row but skipping the outside border for now!
            for x in range(1, width-1): # each width element but skipping outside border
                # count number of neighbors!
                n = 0
                if(twoDBlocks[z+1][x-1]): n += 1
                if(twoDBlocks[z+1][x]): n += 1
                if(twoDBlocks[z+1][x+1]): n += 1
                if(twoDBlocks[z][x-1]): n += 1
                if(twoDBlocks[z][x+1]): n += 1
                if(twoDBlocks[z-1][x-1]): n += 1
                if(twoDBlocks[z-1][x]): n += 1
                if(twoDBlocks[z-1][x+1]): n += 1
                #print(n)
                
                # apply criteria
                if(twoDBlocks[z][x] == 0):
                    if(n == 3):
                        #somehow my z's and x's got switched around
                        mc.setBlock(xo + z, yo, zo + x, blockType)
                        #print('happy birthday cell! at ' + str(x) + ', ' + str(yo) + ', ' + str(z))
                elif n >= 4 or n < 2 :
                    # death by overcrowding or lonliness
                    mc.setBlock(xo + z,yo,zo + x, 0) #just air now!
                    #print( 'cell death at ' + str(x) + ', ' + str(yo) + ', ' + str(z) )
        #time.sleep(1)
    time.sleep(1)
