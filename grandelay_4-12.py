# Module 4-12
# Granular Delay

from earsketch import *

#Initialize new effect:
grainDelay = initEffect('grainDelay')

# create unit generators used by grainDelay:
track = createUGen(grainDelay, INPUT)
noise = createUGen(grainDelay, NOISE)
times = createUGen(grainDelay, TIMES)
delay = createUGen(grainDelay, ECHO)
output = createUGen(grainDelay, OUTPUT)
samp = createUGen(grainDelay, SAMPLEHOLD)
add = createUGen(grainDelay, ADD)

#Connect unit generators according to block diagram:
connect(grainDelay, track, delay)
connect(grainDelay, delay, output)
connect(grainDelay, noise, add)
connect(grainDelay, add, samp)
connect(grainDelay, samp, times)
connect(grainDelay, times, delay, 0, 1)

setParam(add, VALUE, 1)  # need to offset noise output

setParamMin(samp, FREQUENCY, 1)
setParamMax(samp, FREQUENCY, 100)
setParam(samp, FREQUENCY, 40)
createControl(grainDelay, samp, FREQUENCY, 'grainrate (hz)')

setParamMin(times, VALUE, 1)
setParamMax(times, VALUE, 500)
setParam(times, VALUE, 100)
createControl(grainDelay, times, VALUE, 'delay range (ms)')

#Must finish effect before using:
finishEffect(grainDelay)