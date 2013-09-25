# Module 5-9
# Process Music
# Expanding - Retracting Palindrome

from earsketch import *

init()
setTempo(140)

sound = DUBSTEP_DRUMLOOP_MAIN_003

position = 1
for i in range(1, 17):
    duration = 0.0625 * i
    fitMedia(sound, 1, position, position + duration)
    position = position + duration
    
for i in range(0, 16):
    duration = 0.0625 * (16 - i)
    fitMedia(sound, 1, position, position + duration)
    position = position + duration

referenceSound = DUBSTEP_DRUMLOOP_MAIN_001

fitMedia(referenceSound, 2, 1, 18)

finish()