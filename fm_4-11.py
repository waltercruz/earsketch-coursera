# Module 4-9
# Frequency Modulation

from earsketch import *

#Initialize new effect:
fmEffect = initEffect('fmDemo')

# create unit generators used by fmEffect:
carrier = createUGen(fmEffect, SINE)
modulator = createUGen(fmEffect, SINE)
depth = createUGen(fmEffect, TIMES)
base = createUGen(fmEffect, ADD)
output = createUGen(fmEffect, OUTPUT)

#Connect unit generators according to block diagram:
connect(fmEffect, modulator, depth)
connect(fmEffect, depth, base)
connect(fmEffect, base, carrier)
connect(fmEffect, carrier, output)

setParamMin(modulator, FREQUENCY, 1)
setParamMax(modulator, FREQUENCY, 2000)
setParam(modulator, FREQUENCY, 440)
createControl(fmEffect, modulator, FREQUENCY, 'modulator frequency')

setParamMin(depth, VALUE, 1)
setParamMax(depth, VALUE, 1000)
setParam(depth, VALUE, 50)
createControl(fmEffect, depth, VALUE, 'modulation depth')

setParamMin(base, VALUE, 1)
setParamMax(base, VALUE, 1000)
setParam(base, VALUE, 440)
createControl(fmEffect, base, VALUE, 'carrier frequency')

#Must finish effect before using:
finishEffect(fmEffect)