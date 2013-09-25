from earsketch import *

init()

setTempo(120)

sound = HOUSE_DEEP_PIANO_001

fitMedia(sound, 1, 1, 5)

setEffect(1, DISTORTION, DISTO_GAIN, 10)
setEffect(1, PITCHSHIFT, PITCHSHIFT_SHIFT, -2)

finish()