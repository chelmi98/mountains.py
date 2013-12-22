import pyglet
import random

# OPTIONS
WIDTH = 800
HEIGHT = 400
starNumber = 100
RESOLUTION = 7
REDUCTION = 0.65

window = pyglet.window.Window(WIDTH, HEIGHT)

stars = []
for i in xrange(starNumber):
    stars += [random.randint(0, WIDTH)] # x value
    stars += [random.randint(0, HEIGHT)] # y value

def draw_stars():
    pyglet.graphics.draw(len(stars)/2, pyglet.gl.GL_POINTS, ('v2i', stars))

class segment():
    def __init__(self, height, offset, noise, color):
        points = [(0, height), (WIDTH, height)]

        for i in range(RESOLUTION):
            b = len(points)-1
            for c in range(b):
                points.insert((c*2)+1, (
                    ((points[c*2][0]+points[(c*2)+1][0])/2),
                    ((points[c*2][1]+points[(c*2)+1][1])/2)+
                        random.randint(int(-noise), int(noise))))
            noise *= REDUCTION

        verts = []

        for i in xrange(len(points)-1):
            verts += [
                points[i][0]+offset, 0, # btm L
                points[i+1][0]+offset, 0, # btm R
                points[i+1][0]+offset, points[i+1][1], # upr R
                points[i][0]+offset, points[i][1]] # upr L

        self.verts = verts
        self.color = color

    def update(self, offset):
        for i in xrange(len(self.verts)/2):
            self.verts[i*2] -= offset

    def draw(self):
        pyglet.graphics.draw(len(self.verts)/2, pyglet.gl.GL_QUADS,
            ('v2i', self.verts),
            ('c3B', self.color*(len(self.verts)/2))
        )

mtn1 = [segment(200, WIDTH, 50, (50, 71, 107)),
        segment(200, 0, 50, (50, 71, 107))]
mtn1o = 0
mtn2 = [segment(150, WIDTH, 50, (30, 46, 74)),
        segment(150, 0, 50, (30, 46, 74))]
mtn2o = 0
mtn3 = [segment(100, WIDTH, 50, (16, 25, 41)),
        segment(100, 0, 50, (16, 25, 41))]
mtn3o = 0
mtn4 = [segment(50, WIDTH, 50, (6, 12, 23)),
        segment(50, 0, 50, (6, 12, 23))]
mtn4o = 0

def update(dt):
    global mtn1o, mtn2o, mtn3o, mtn4o

    if mtn1o == WIDTH:
        mtn1.pop(1)
        mtn1.insert(0, segment(200, WIDTH, 50, (50, 71, 107)))
        mtn1o = 0
    else:
        mtn1[0].update(1)
        mtn1[1].update(1)
        mtn1o += 1

    if mtn2o == WIDTH:
        mtn2.pop(1)
        mtn2.insert(0, segment(150, WIDTH, 50, (30, 46, 74)))
        mtn2o = 0
    else:
        mtn2[0].update(2)
        mtn2[1].update(2)
        mtn2o += 2

    if mtn3o == WIDTH:
        mtn3.pop(1)
        mtn3.insert(0, segment(100, WIDTH, 50, (16, 25, 41)))
        mtn3o = 0
    else:
        mtn3[0].update(4)
        mtn3[1].update(4)
        mtn3o += 4

    if mtn4o == WIDTH:
        mtn4.pop(1)
        mtn4.insert(0, segment(50, WIDTH, 50, (6, 12, 23)))
        mtn4o = 0
    else:
        mtn4[0].update(8)
        mtn4[1].update(8)
        mtn4o += 8

pyglet.clock.schedule_interval(update, 1/30.0)

@window.event
def on_draw():
    global offset
    window.clear()
    pyglet.graphics.draw(4, pyglet.gl.GL_QUADS,
        ('v2i', (0, 0, WIDTH, 0, WIDTH, HEIGHT, 0, HEIGHT)),
        ('c3B', (0, 0, 0, 0, 0, 0, 25, 17, 31, 25, 17, 31))
    )
    draw_stars()
    mtn1[0].draw()
    mtn1[1].draw()
    mtn2[0].draw()
    mtn2[1].draw()
    mtn3[0].draw()
    mtn3[1].draw()
    mtn4[0].draw()
    mtn4[1].draw()

pyglet.app.run()
