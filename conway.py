#Minecraft Conway's Game of Life
#Blocks live, die, or are born by the cruel rules of nature
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
# well enough to fix this.  It's not returning as I excpect, only if it's a
# square array
width = 50
depth = 50

# manually wrote a non square array to test logic below, it works just fine.
#blocks = [0] * 2500 # simulate 50 x 50 grid # standalone
#newBlocks = [0] * 2500 # a place to put the results in for standalone testing

ticks = 0;
while 1: # Infinite loop!
    # my 'ON' switch for the simulation is just a space, if it has a block in it,
    # the code runs.
    onSwitch = mc.getBlock(-94, 83, 78);
    if onSwitch: # if it's there, the code runs!

        # get the width and height worth of blocks from the world, comment out for stand-alone
        blocks = mc.getBlocks(xo, yo, zo, xo+width-1, yo, zo+depth-1)
        
        # The 'blocks' returned from mc.getBlocks are in single comma separated list.
        # split up the result into depth-number of rows in an array of width-number columns
        twoDBlocks = []
        test = 0 # a variable to increment while splitting up the array
        for z in range(depth):
            twoDBlocks.append( blocks[test : test + width] )
            test += width

        # find the number of neighbors! 
        for z in range(1, depth - 1): # each row but skipping the outside border for now!
            for x in range(1, width - 1): # each width element but skipping outside border
                # count number of neighboring cells for each cell in array
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
                
                # apply criteria for Conway's life:
                # if an empty cell has exactly 3 occupied neighbors, a new cell is born
                # if an occupied cell has < 2 neighbors, it dies from lonliness or starvation.
                # if an occupied cell has > 3 neighbors, it dies from suffocation or overcrowding.
                if(twoDBlocks[z][x] == 0):
                    if(n == 3):
                        # TODO fix the logic, somehow my z's and x's got switched around
                        mc.setBlock(xo + z, yo, zo + x, blockType)
                        #newBlocks[z][x] = blockType # for standalone
                        #print('happy birthday cell! at ' + str(x) + ', ' + str(yo) + ', ' + str(z))
                elif n >= 4 or n < 2 :
                    # death by overcrowding or lonliness
                    mc.setBlock(xo + z,yo,zo + x, 0) #just air now!
                    #newBlocks[z][x] = 0 # for standalone
                    #print( 'cell death at ' + str(x) + ', ' + str(yo) + ', ' + str(z) )
        #time.sleep(1)
        ticks += 1
        #blocks = newBlocks # only needed for standalone testing.
        print(ticks)
    #time.sleep(1)
