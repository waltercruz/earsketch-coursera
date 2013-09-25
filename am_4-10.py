# Module 4-8
# Amplitude Modulation

from earsketch import *

#Initialize new effect:
amEffect = initEffect('amWithSlider')

# create unit generators used by amEffect:
inp = createUGen(amEffect, INPUT)
sin = createUGen(amEffect, SINE)
times = createUGen(amEffect, TIMES)
output = createUGen(amEffect, OUTPUT)

#Connect unit generators according to block diagram:
connect(amEffect, inp, times, 0, 0)
connect(amEffect, sin, times, 0, 1)
connect(amEffect, times, output)

#Set the min, max, and default sin wave frequency:
setParamMin(sin, FREQUENCY, 5)     #audible range is about 20 to 20,000 (hz)
setParamMax(sin, FREQUENCY, 5000)  #min and max will set range of control slider
setParam(sin, FREQUENCY, 200)      #this will be the default control slider value
createControl(amEffect, sin, FREQUENCY, 'modulator frequency')

#Must finish effect before using:
finishEffect(amEffect)