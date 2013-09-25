# Module 5-7
# Chance Music

from earsketch import *
from random import *

init()
tempo = randint(60, 180)
setTempo(tempo)

soundFolder = RICHARDDEVINE__DUBSTEP_140_BPM__DUBDRUM
stopMeasure = 8

for i in range(randint(50, 150)):
    sound = selectRandomFile(soundFolder)
    track = randint(1, 16)
    start = random() * stopMeasure
    end = start + random()
    fitMedia(sound, track, start, end)

finish()