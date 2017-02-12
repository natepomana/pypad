
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

        pygame.mixer.init()
        pygame.mixer.music.load('spectre.wav')
        pygame.mixer.music.play()

	


	print('at individual light')	
	lp.LedCtrlXY(0,0,100,0,0)
	pygame.time.wait(500)
	#forget coordinates, doesn't wipe visuals.


	#check above
	scroll_vert(3,lp)
	scroll_vert(2,lp)
	pygame.time.wait(200)

	wipe_vert(3,lp)
	wipe_vert(2,lp)

	scroll_vert(7,lp)
	
	#resets colors
	lp.Reset()
	


	pygame.time.wait(2000)


	lp.Reset() # turn all LEDs off
	lp.Close() # close the Launchpad (will quit with an error due to a PyGame bug)

	
if __name__ == '__main__':
	main()

