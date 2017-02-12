	
import sys

try:
	import launchpad_py as launchpad
except ImportError:
	try:
		import launchpad
	except ImportError:
		sys.exit("error loading launchpad.py")

import random
import pygame
import fade

def clear(lp):
	lp.Reset()
	lp.ButtonFlush()



def scroll_vert(vert,lp,time):
	# 8 because hight is 8
	# while loop, color is red and waits 50ms before changing next one
	but = 8
	while (but > 0):
		lp.LedCtrlXY(vert,but,random.randint(0,63),random.randint(0,63),random.randint(0,63))
		but -= 1
		pygame.time.wait(time)	

def wipe_vert(vert, lp,time):
	#erase all color in vertical col
	but = 8
	while (but > 0):
		lp.LedCtrlXY(vert,but,0,0,0)
		but -= 1
		pygame.time.wait(time)


def scroll_horz(horz,lp,time):
        # 8 because hight is 8
        # while loop, color is red and waits 50ms before changing next one
        but = 8
        while (but >=  0):
                lp.LedCtrlXY(but,horz,random.randint(0,63),random.randint(0,63),random.randint(0,63))
                but -= 1
                pygame.time.wait(time)

def wipe_horz(horz, lp,time):
        #erase all color in vertical col
        but = 8
        while (but >=  0):
                lp.LedCtrlXY(but,horz,0,0,0)
                but -= 1
                pygame.time.wait(time)


def fill_vert(lp,time):
	for x in range(8):
		for y in range(8):
			lp.LedCtrlXY(x,y+1,random.randint(0,63),random.randint(0,63),random.randint(0,63))
			pygame.time.wait(time)
	
def fill_horz(lp,time):
	for y in range(8):
                for x in range(8):
                        lp.LedCtrlXY(x,y+1,random.randint(70,100),random.randint(70,100),random.randint(70,100))
                        pygame.time.wait(time)


def heart(lp):
	lp.LedCtrlXY(1,2,100,0,0)
	lp.LedCtrlXY(2,2,100,0,0)
	lp.LedCtrlXY(5,2,100,0,0)
	lp.LedCtrlXY(6,2,100,0,0)
	lp.LedCtrlXY(0,3,100,0,0)
	lp.LedCtrlXY(3,3,100,0,0)
	lp.LedCtrlXY(4,3,100,0,0)
	lp.LedCtrlXY(7,3,100,0,0)
	lp.LedCtrlXY(0,4,100,0,0)
	lp.LedCtrlXY(7,4,100,0,0)
	lp.LedCtrlXY(1,5,100,0,0)
	lp.LedCtrlXY(6,5,100,0,0)
	lp.LedCtrlXY(5,6,100,0,0)
	lp.LedCtrlXY(2,6,100,0,0)
	lp.LedCtrlXY(3,7,100,0,0)
	lp.LedCtrlXY(4,7,100,0,0)

def swipe_right(lp,time):
	row = 8
	while (row >=  0):
		scroll_vert(row,lp,0)
		wipe_vert(row+1,lp,0)
		pygame.time.wait(time)
		row -= 1
	wipe_vert(0,lp,0)

def swipe_left(lp,time):
        col = 0
        while (col <=  8):
                scroll_vert(col,lp,0)
                wipe_vert(col-1,lp,0)
                pygame.time.wait(time)
                col += 1
        wipe_vert(8,lp,0)

def swipe_up(lp,time):
        row = 8
        while (row >= 0):
                scroll_horz(row,lp,0)
                wipe_horz(row+1,lp,0)
                pygame.time.wait(time)
                row -= 1
        wipe_horz(0,lp,0)


def swipe_down(lp,time):
        row = 0
        while (row <=  8):
                scroll_horz(row,lp,0)
                wipe_horz(row-1,lp,0)
                pygame.time.wait(time)
                row += 1
        wipe_horz(8,lp,0)

def border(lp,lev):
	# lev - depth of square.
	"""
	check what level it's at.
	0-3, 1 is farthest out, 4 is center
	that value is the x-value.
	
	lev=1
	far = 8-lev
	x = 8-lev
	y = 8-lev
	while x > 0:
		lp.colorshit(x,far,0,100,10)
	"""

	#left and right	
	max = 8-lev
	l_bar = lev
	count = lev+1
	while (count <= max):
		lp.LedCtrlXY(l_bar,count,0,0,100)
		lp.LedCtrlXY(max-1,count,0,0,100)
		count += 1
	
	#top and bot
	count = lev+1
	top = count
	bot = 8-lev
	t_bar = lev
	while(count < max):
		lp.LedCtrlXY(count,top,0,0,100)
		lp.LedCtrlXY(count,bot,0,0,100)
		count += 1
		
def top_triangle	



def main():
	mode = None

	# create an instance
	lp = launchpad.Launchpad()
	# check what we have here and override lp if necessary
	if lp.Check( 0, "mk2" ):
		lp = launchpad.LaunchpadMk2()
		if lp.Open( 0, "mk2" ):
			print("Loaded")
			mode = "Mk2"

	# Clear the buffer because the Launchpad remembers everything :-)
	lp.LedCtrlXY(0,0,1,0,0)
	lp.ButtonFlush()
	lp.Reset()

        pygame.mixer.init()
        pygame.mixer.music.load('spectre.wav')
        pygame.mixer.music.play()
	pygame.time.wait(500)

	
	scroll_vert(0,lp,50)
	scroll_vert(7,lp,50)
	pygame.time.wait(200)

	wipe_vert(0,lp,50)
	wipe_vert(7,lp,50)

	#outside border
	scroll_vert(8,lp,50)
	scroll_horz(0,lp,50)
	pygame.time.wait(100)
	wipe_vert(8,lp,50)
	wipe_horz(0,lp,50)
	
	

	#resets colors
	lp.Reset()
	

	fade.run_fade(8,8,lp)
	clear(lp)

	fill_vert(lp,20)

	fill_horz(lp,20)

	fade.run_fade(8,8,lp)

	clear(lp)	

	heart(lp) 

	pygame.time.wait(1000)

	lp.Reset()

	swipe_right(lp,20)

	swipe_left(lp,0)

	swipe_up(lp,50)

	swipe_down(lp,70)
	
	border(lp,0)
	pygame.time.wait(1000)

	clear(lp)	
	
	border(lp,1)		
	pygame.time.wait(900)

	clear(lp)	

	border(lp,2)
	pygame.time.wait(900)

	clear(lp)
	border(lp,3)

	pygame.time.wait(1000)

	clear(lp)

	#lp.Reset() # turn all LEDs off
	lp.Close() # close the Launchpad (will quit with an error due to a PyGame bug)

	
if __name__ == '__main__':
	main()

