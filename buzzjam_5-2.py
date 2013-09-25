# setup
from earsketch import *

init()
setTempo(120)

# variables

introScratch  = HOUSE_MAIN_BEAT_001
introWhoosh   = TECHNO_WHITENOISESFX_006 
introDrumfill = ELECTRO_DRUM_MAIN_BEAT_003
drums1 = TECHNO_KICKROLL_001
lead  = ELECTRO_ANALOGUE_LEAD_013
bass1  = TECHNO_ACIDBASS_008
synth1 = TECHNO_CLUBRICH_PAD_001 
floor = TECHNO_MAINLOOP_018
drums2  = TECHNO_SNAREROLL_001
synth2  = DUBSTEP_FILTERCHORD_002 
plucks = TECHNO_SYNTHPLUCK_001
bass2   = TECHNO_ACIDBASS_006
drumbreak  =ELECTRO_DRUM_MAIN_BEAT_002
voxfx  = EIGHT_BIT_VIDEO_SPEAKNSPELL_BEAT_007

beatHit = TECHNO_MAINLOOP_008
beatString = "0---0---0--0-0-0" #  specifies a rhythmic pattern of 16th notes

# Intro

fitMedia(synth2, 5, 1, 5)
fitMedia(introScratch, 8, 1, 5)
fitMedia(plucks,   9, 3, 5)
fitMedia(introWhoosh, 10, 1.75, 5)
fitMedia(introDrumfill, 6, 4, 5)

# A Section (simplest version)

fitMedia(drums1, 1, 5, 9)
fitMedia(synth1, 2, 5, 9)
fitMedia(lead, 11, 5, 9)  

# A Section (more parts added)

fitMedia(drums1, 1, 9, 13)    # plays all through section A (4 bars)
fitMedia(synth1, 2, 9, 13)
fitMedia(floor, 3, 9, 13)
fitMedia(lead, 11, 9, 13)
fitMedia(bass1, 12, 9.125, 13)

# B Section (contrasting section)

fitMedia(drums2,  1, 13, 17)
fitMedia(drumbreak,  4, 13, 17)
fitMedia(synth2,  5, 13, 17)
fitMedia(plucks, 9, 13, 17)
fitMedia(bass2,  13, 13, 17) 
makeBeat(beatHit, 6, 13, beatString)
makeBeat(beatHit, 6, 15, beatString)

# A Section (more parts added)

fitMedia(drums1, 1, 17, 23)
fitMedia(synth1, 2, 17, 23)
fitMedia(floor, 3, 17, 23)
fitMedia(lead, 11, 17, 23)
fitMedia(bass1, 12, 17.125, 23)
fitMedia(voxfx,  7, 17, 18)
fitMedia(voxfx,  7, 19, 20)
fitMedia(voxfx,  7, 21, 22)
makeBeat(beatHit, 6, 19, beatString)
makeBeat(beatHit, 6, 21, beatString)

# Ending

fitMedia(synth2,  5, 23, 24)
fitMedia(voxfx,   7, 23, 24.9375)
fitMedia(introDrumfill, 6, 23, 24.125)

# effects

# set volumes on tracks
setEffect(1, VOLUME, GAIN, 1.5) # setting volumes on some tracks to help move toward a good mix of all sounds
setEffect(2, VOLUME, GAIN, 0)  # since the volume level of this track sounds good at 0, we don't need to call this (but we still could, with volume value 0 as shown)
setEffect(3, VOLUME, GAIN, -2)
setEffect(4, VOLUME, GAIN, 3)
setEffect(5, VOLUME, GAIN, -4.5)
setEffect(6, VOLUME, GAIN, -5.5)
setEffect(7, VOLUME, GAIN, -6)
setEffect(8, VOLUME, GAIN, -3)
setEffect(9, VOLUME, GAIN, -4.5)
setEffect(10, VOLUME, GAIN, -22)
setEffect(11, VOLUME, GAIN, -11)
setEffect(12, VOLUME, GAIN, -4)
setEffect(13, VOLUME, GAIN, -4)

setEffect(6, DISTORTION, DISTO_GAIN, 12)

# add some delay

setEffect(5, PITCHSHIFT, PITCHSHIFT_SHIFT, 2)  # pad chord sound
setEffect(5,  DELAY, DELAY_MIX, 0.75) 
setEffect(5,  DELAY, DELAY_TIME, 782) # this delay time value (in ms) makes a dotted-4tr note pulse (for 115 bpm)
setEffect(6,  DELAY, DELAY_MIX, 0.38) # beatHit sound
setEffect(6,  DELAY, DELAY_TIME, 391) # this delay time value (in ms) makes a dotted-8th note pulse (for 115 bpm)
setEffect(8,  DELAY, DELAY_MIX, 0.38) # intro scratch sound
setEffect(8,  DELAY, DELAY_TIME, 391) # this delay time value (in ms) makes a dotted-8th note pulse (for 115 bpm)
setEffect(9,  DELAY, DELAY_MIX, 0.38) # intro synth sound
setEffect(9,  DELAY, DELAY_TIME, 522) # this delay time value (in ms) makes a quarter note pulse (for 115 bpm)
setEffect(10, DELAY, DELAY_MIX, 0.38) # intro whoosh sound
setEffect(10, DELAY, DELAY_TIME, 522) # this delay time value (in ms) makes a quarter note pulse (for 115 bpm)

finish()
