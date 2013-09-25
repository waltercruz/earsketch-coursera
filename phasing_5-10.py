from earsketch import *

init()
setTempo(220)

sound = ELECTRO_ANALOGUE_LEAD_010

def doTrack(track, duration, pan):
    position = 1
    for i in range(32):
      fitMedia(sound, track, position, position + duration)
      position = position + duration
    setEffect(track, PAN, LEFT_RIGHT, pan)

doTrack(1, 2, -100)
doTrack(2, 1.95, 100)
#doTrack(3, 1.9, 0)
#doTrack(4, 1.85, -50)
#doTrack(5, 1.8, 50)

#finish section
finish()