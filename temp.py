
import sys

try:
	import launchpad_py as launchpad
except ImportError:
	try:
		import launchpad
	except ImportError:
		sys.exit("error loading launchpad.py")

import random
from pygame import time


def wait():
	time.wait(50)

def scroll(lp):
	but = 8
	while (but > 0):
		lp.LedCtrlXY(3,but,100,0,0)
		but -= 1
	



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
	lp.ButtonFlush()
	print('at individual light')	
	lp.LedCtrlXY(0,0,100,0,0)
	lp.LedCtrlXY(1,1,100,0,0)
	lp.LedCtrlXY(2,2,100,0,0)
	lp.LedCtrlXY(3,3,100,0,0)

	time.wait(500)
	print('flushing')
	lp.ButtonFlush()

<<<<<<< HEAD
	scroll(lp)
	time.wait(4000)
=======
	lp.LedCtrlXY(1,1,0,64,0,0)
	print('attempting sound')
	if lp.LedCtrlXY(1,1,0,64,0,0):
		pygame.mixer.init()
		pygame.mixer.load('01.wav')
		pygame.mixer.play()
	


	# Lightshow
	butHit = 0
	while 1:
		lp.LedCtrlRaw( random.randint(0,127), random.randint(0,63), random.randint(0,63), random.randint(0,63) )
		time.wait( 50 )
		
		but = lp.ButtonStateRaw()
		if but != []:
			butHit += 1
			print( butHit, " button: ", but )
			if butHit > 10:
				break
>>>>>>> b368a08a88273a819bcd1c58a0d31d9bc23002b1


	lp.Reset() # turn all LEDs off
	lp.Close() # close the Launchpad (will quit with an error due to a PyGame bug)

	
if __name__ == '__main__':
	main()

