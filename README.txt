COLLIDING BLOCKS by Antonio Foglia


Quickstart
----------

Run main_visual.py and have fun!


Intro
-----

This project was inspired by a 3Blue1Brown video: https://www.youtube.com/watch?v=jsYwFizhncE.

The ideas is that two blocks colliding with each other and a wall will
produce pi collisions if the mass factor between the blocks is a power of
100.

Running
-------

main_code.py:
  This is the main version which will output the number of collisions given
  initial parameters. It works well for powers of 100 up to 6 although
  runtime is quite large.

main_visual.py:
  This is the version with a visual implementation. It uses the turtle
  python library to render the blocks. It works well for powers of 100 up to
  2. Use main_code.py for higher powers.

Other folders:

two_walls:
  This is a working visual implementation of the code with walls on either
  side of the blocks.

testing:
  These are the jupyter notebooks I used for the development of the project.

sounds:
  Where the sounds for the visual version are stored.
