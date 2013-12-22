mountains.py
============
I decided to make a simple (and poorly coded) example pyglet and a terrain generation algorithm. I used the midpoint displacement fractal method for the mountains, which is surprisingly fast and simple. It basically works by taking two points and raising or lowering the midpoint by a random amount. By repeating this, you can get some pretty cool results. Hopefully, you can learn something from this project.
Usage
-----
To run this program you need to have both python and pyglet installed. I'll asume you have python. If you dont, go [here]( http://www.python.org/download/releases/2.7.6/). Back to pyglet, if you have pip installed, open up the terminal and type
```
pip install pyglet
```
Otherwise, go to http://www.pyglet.org/download.html and follow the instructions there. Once you have pyglet installed, you can go ahead and run the program.
###Screenshot:
![screenshot](screenshot.png)
