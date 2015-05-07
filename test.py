from psychopy import visual, core 
from psychopy.visual import DotStim

# Create a DotStim, which is automatically updated with every `draw()` call.
win = visual.Window([800,600], monitor="testMonitor", units="deg")
ds = DotStim(win, fieldSize=17, speed=.01, dotSize=4,dir=0,dotLife=10, nDots=50, coherence=.2,fieldShape='circle')

# Show 1000 frames

for i in range(1000):
    ds.draw()
    win.flip()
    win.getMovieFrame()

win.saveMovieFrames("test_images/images.png")

#http://www.cogsci.nl/forum/index.php?p=/discussion/879/open-random-dot-motion/p1
