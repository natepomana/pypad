
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



def scroll_vert(vert,lp):
	# 8 because hight is 8
	# while loop, color is red and waits 50ms before changing next one
	but = 8
	while (but > 0):
		lp.LedCtrlXY(vert,but,100,0,0)
		but -= 1
		pygame.time.wait(50)	

def wipe_vert(vert, lp):
	#erase all color in vertical col
	but = 8
	while (but > 0):
		lp.LedCtrlXY(vert,but,0,0,0)
		but -= 1
		pygame.time.wait(50)


def scroll_horz(horz,lp):
        # 8 because hight is 8
        # while loop, color is red and waits 50ms before changing next one
        but = 8
        while (but > 0):
                lp.LedCtrlXY(but,horz,100,0,0)
                but -= 1
                pygame.time.wait(50)

def wipe_horz(horz, lp):
        #erase all color in vertical col
        but = 8
        while (but > 0):
                lp.LedCtrlXY(but,horz,0,0,0)
                but -= 1
                pygame.time.wait(50)


def fill_vert(lp,time):
	for x in range(8):
		for y in range(8):
			lp.LedCtrlXY(x,y+1,0,0,100)
			pygame.time.wait(time)
	
def fill_horz(lp,time):
	for y in range(8):
                for x in range(8):
                        lp.LedCtrlXY(x,y+1,0,50,10)
                        pygame.time.wait(time)




def main():
	mode = None

	# create an instance
	lp = launchpad.Launchpad();

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

	
	scroll_vert(3,lp)
	scroll_vert(2,lp)
	pygame.time.wait(200)

	wipe_vert(3,lp)
	wipe_vert(2,lp)

	#outside border
	scroll_vert(8,lp)
	scroll_horz(0,lp)
	pygame.time.wait(100)
	wipe_vert(8,lp)
	wipe_horz(0,lp)
	
	

	#resets colors
	lp.Reset()
	

	fade.run_fade(8,8,lp)
	lp.ButtonFlush()
	print('first fade')
	lp.Reset()
	lp.ButtonFlush

	fill_vert(lp,20)

	fill_horz(lp,20)

	fade.run_fade(8,8,lp)

	pygame.time.wait(2000)


	#lp.Reset() # turn all LEDs off
	lp.Close() # close the Launchpad (will quit with an error due to a PyGame bug)

	
if __name__ == '__main__':
	main()

