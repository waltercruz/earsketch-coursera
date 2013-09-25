# Module 4 - 5
# Our second EarSketch Script
# Creating a slider to set multiply value

from earsketch import *

#Initialize new effect:
volumeEffect = initEffect('sliderVolume')

#create ugens used by volumeEffect:
track = createUGen(volumeEffect, INPUT)
multiply = createUGen(volumeEffect, TIMES)
out = createUGen(volumeEffect, OUTPUT)

#Connect ugens according to block diagram:
connect(volumeEffect, track, multiply)  # INPUT is connected to TIMES
connect(volumeEffect, multiply, out)     # TIMES is connected to OUTPUT

#set the multiplier
setParamMin(multiply, VALUE, 0)
setParamMax(multiply, VALUE, 1)
setParam(multiply, VALUE, 0.25) # sets default multiply to 0.25
createControl(volumeEffect, multiply, VALUE, 'multiplier')

#Must finish effect before using:
finishEffect(volumeEffect)