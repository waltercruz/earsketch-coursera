# Module 5-8
# Chance Music

from earsketch import *
from random import *

init()
setTempo(120)

soundFolder = RICHARDDEVINE__DUBSTEP_140_BPM__DUBDRUM

for measure in range(1, 9):
    sound = selectRandomFile(soundFolder)
    fitMedia(sound, 1, measure, measure + 1)

finish()