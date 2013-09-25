# Module 4-8
# Subtractive Synthesis

from earsketch import *

#Initialize new effect:
subtractive = initEffect('basicFilters')

baseFreq = 100
track = createUGen(subtractive, INPUT)
output = createUGen(subtractive, OUTPUT)

# create and connect ugens: (note that there is no input)
for i in range(10):
    harmonic = i + 1
    freq = baseFreq * harmonic
    bandpass = createUGen(subtractive, BANDPASS)
    setParam(bandpass, FREQUENCY, freq)
    setParam(bandpass, RESONANCE, 1.5)
    connect(subtractive, track, bandpass)
    connect(subtractive, bandpass, output)

#Must finish effect before using:
finishEffect(subtractive)