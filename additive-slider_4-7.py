# Module 4-6
# Additive Synthesis with slider control of frequency

from earsketch import *

#Initialize new effect:
additive = initEffect('sliderAdd')

output = createUGen(additive, OUTPUT)
baseFreq = createUGen(additive, NUMBER)

# create ugens: (no input)
for i in range(5):
    harmonic = i + 1
    freqMult = createUGen(additive, TIMES)
    osc = createUGen(additive, SINE)
    times = createUGen(additive, TIMES)
    setParam(freqMult, VALUE, harmonic)
    setParam(times, VALUE, 1.0 / harmonic)
    println(1.0 / harmonic)
    connect(additive, baseFreq, freqMult)
    connect(additive, freqMult, osc)
    connect(additive, osc, times)
    connect(additive, times, output)
    
setParamMin(baseFreq, VALUE, 20)
setParamMax(baseFreq, VALUE, 2000)
setParam(baseFreq, VALUE, 440)
createControl(additive, baseFreq, VALUE, 'base frequency')

#Must finish effect before using:
finishEffect(additive)