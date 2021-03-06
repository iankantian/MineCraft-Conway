# MineCraft Conway's Game of Life
=======
Joshua Brown 2016

This is a Python script that runs according to the rules of [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life), the most famous example of [Cellular Automaton](https://en.wikipedia.org/wiki/Cellular_automaton).
What is remarkable about Conway's Game is that complex emergent behaviors arise from profoundly simple rules:
* the world is a 2d grid of cells that are occupied, 'alive' or empty, 'dead'
* if an empty cell has exactly 3 neighbors, that cell becomes 'alive' as if by reproduction
* if an occupied cell has 2 or 3 neighbors it survives to the next generation
* if an occupied cell has only 1 neighbor it dies as if by starvation or lonliness
* if an occupied cell has 4 or more neighbors it dies as if by overcrowding or suffocation

Recreational mathmeticians usually experience the game from an omnipotent and disconnected top-down approach.  With this script you can walk amongst the life, interacting at 'eye-level' with the simulation.

To display the iterating generations, I am using a [MineCraft world](https://minecraft.net).
![Conway](https://lh3.googleusercontent.com/PUhROTcC6Ci0qlBQXaNoDvbhmAYO51kvEBxkaxF45CTzNzng8Y1O8HscCD9rve3WOqITEXR6rRyVq1k9ku8EuP4cOCs_bP8hY1FNE6hnLqYDy7v2i3kfQHm_gsPNjaKU2-xTHAJehE4SbxrIouWO_2I4PqA4X8xtKmsO0pTl-PB9vDd1aVtRE51DTaPG8yw16TT2TacAj8lGYd52G6AgbsP7MsgynDbk1e1mAO3oZd0ujn_LVqUhGh_pJs4yomOQUiTAlxxiCrlT_URzULBf1wjbfhvMAElX3nDTnxU8Cw0cEJKqwQ5yad8PExkAW6YUIpLbIy51IUjn8uoV1YL2KB_qpeZdVjHYAoYQnDT7u5rMf1KMeHvg6lmXFyUg4vSVRDNh-CY7p4Y6HQlBSudsykUVHr6QxdWYb-XqZ7L8ennK2mqXKhrPikv79Pg7E3grnRE5Q23mcf-3BXO70pRFj6Aj4cA2lSgfWFUTVW29r-E5ZS_c9h_5Fwe5aowUdoqdXTRWJAoOTPSJgy-LRzz1uwd6fhpPy7T5IQZlnEl49YuqWrgUK1JevkDQWk7L2sm2nUvFr3ZqFJkjnrvKNMZx5h-IWt2KNBM=w1822-h1140-no)

The world grid is in a [Minecraft Bukkit Server](http://wiki.bukkit.org).  But later I'd like to switch to [Forge](http://files.minecraftforge.net), as that allows the use of the [HTC Vive](https://www.htcvive.com) for a VR experience with Python.

The [RasberryJuice Plugin](http://dev.bukkit.org/bukkit-plugins/raspberryjuice/) runs on Bukkit, allowing you to import the api for Python script control.  Potentially for use with Forge 

Be aware for using this script that you have to edit your initial coordinates 'xo, yo, zo' to a good lower left corner of your own Minecraft world.  Also, the test for running the loop is whether a block is at a certain x,y,z.  I chose an arbitrary point for a sticky piston to remove a block from that location to stop the loop from running.

TODO  
Add some modules to populate game with a game grid, clearig the grid, and little pre-made modules like Gosper Glider that can be loaded up.

Logic for the block setting code got x and z swapped.  My hack was to swap x and z in the setBlocks arguments.  Not ideal.

See if it's more efficient to set the next generation of the game grid all at once.  I'm not so sure it is, as the API is pretty efficient as-is.

Acknowledgements
A book that is a decent beginner's programming guide, that dives right into scripting MineCraft, is ["Learn to Program with Minecraft"](https://www.nostarch.com/programwithminecraft), Craig Richardson, No Starch Press, 2016.  This project isn't from that book.  But I did use the first chapter to set up my build environment.  For example it pointed me to these scripts which made setup so much easier.
* [Some setup downloads to make setting up easier](https://www.nostarch.com/programwithminecraft)

