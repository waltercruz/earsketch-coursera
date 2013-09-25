# Module 6-1

from earsketch import *

# initialize Reaper
init()
setTempo(120)

# set up my parameters for this run
sound1 = ELECTRO_DRUM_MAIN_BEAT_001
sound2 = ELECTRO_DRUM_MAIN_BEAT_002
analysisMethod = SPECTRAL_CENTROID
hop = 0.0625  # analyze in 1/16th note chunks
start = 1
end = 3
numChunks = 32

# insert audio on two tracks
fitMedia(sound1, 1, start, end)
fitMedia(sound2, 2, start, end)

# analyze each beat and set volume effect accordingly
for i in range(numChunks):
    position = 1 + i * hop
    feature1 = analyzeTrackForTime(1, analysisMethod, position, position + hop)
    feature2 = analyzeTrackForTime(2, analysisMethod, position, position + hop)
    if (feature1 > feature2):
        setEffect(1, VOLUME, GAIN, 0, position, 0, position + hop)
        setEffect(2, VOLUME, GAIN, -60, position, -60, position + hop)
    else:
        setEffect(1, VOLUME, GAIN, -60, position, -60, position + hop)
        setEffect(2, VOLUME, GAIN, 0, position, 0, position + hop)
    
# we're done
finish()
