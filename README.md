# MineCraft Conway's Game of Life
Joshua Brown 2016

This is a Python script that runs according to the rules of Conway's Game of Life.

The world grid is in a Minecraft Bukkit Server.

The RasberryJuice Plugin runs on Bukkit, allowing you to import the api for Python script control.

A book that is a decent beginner's programming guide, that dives right into scripting MineCraft, is
"Learn to Program with Minecraft", Craig Richardson, No Starch Press, 2016.  This project isn't from that book, but having a professionally written and published procedure to get the build environment up and running was worth the price of the book.

Be aware that you have to edit your initial coordinates 'xo, yo, zo' to a good lower left corner of your own Minecraft world.  Also, the test for running the loop is whether a block is at a certain x,y,z.  I chose an arbitrary point for a sticky piston to remove a block from that location to stop the loop from running.

