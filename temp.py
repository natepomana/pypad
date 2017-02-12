
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

	lp.LedCtrlXY(4,8,100,0,0)

	time.wait(5000)
	print('flushing')
	lp.ButtonFlush()


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


	lp.Reset() # turn all LEDs off
	lp.Close() # close the Launchpad (will quit with an error due to a PyGame bug)

	
if __name__ == '__main__':
	main()

