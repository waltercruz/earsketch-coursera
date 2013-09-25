from earsketch import *

init()

setTempo(120)

sound = HOUSE_DEEP_PIANO_001

fitMedia(sound, 1, 1, 5)

setEffect(1, DISTORTION, DISTO_GAIN, 0, 1, 20, 5)
setEffect(1, PITCHSHIFT, PITCHSHIFT_SHIFT, -2, 1, 0, 3)
setEffect(1, PITCHSHIFT, PITCHSHIFT_SHIFT, 0, 3, -6, 5)

finish()