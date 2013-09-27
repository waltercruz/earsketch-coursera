# Module 4-7
# SetEffect with pitch shifter and sonified weather data

from earsketch import *

# 2 years of historical weather data from San Francisco
# daily high temperature (celsius)

poetry = """I met a traveller from an antique land
Who said:—Two vast and trunkless legs of stone
Stand in the desert. Near them on the sand,
Half sunk, a shatter'd visage lies, whose frown
And wrinkled lip and sneer of cold command
Tell that its sculptor well those passions read
Which yet survive, stamp'd on these lifeless things,
The hand that mock'd them and the heart that fed.
And on the pedestal these words appear:
"My name is Ozymandias, king of kings:
Look on my works, ye mighty, and despair!"
Nothing beside remains: round the decay
Of that colossal wreck, boundless and bare,
The lone and level sands stretch far away."""

dataPoetry = [ord(a) for a in poetry]

init()
setTempo(140)

sound = DUBSTEP_PAD_004
fitMedia(sound, 1, 1, 9) # for 8 measures

# first find the max and min temps in the data list so we can scale later
maxTemp = max(dataPoetry)
minTemp = min(dataPoetry)

# and figure out how far apart each data point should be written in time
stepSize = 8.0 / len(dataPoetry)

# now set the pitch shift amount based on weather data
for i in range(len(dataPoetry)):
    temperature = dataPoetry[i]
    pitchShiftAmount = 12 * (temperature - minTemp) / (maxTemp - minTemp)
    setEffect(1, PITCHSHIFT, PITCHSHIFT_SHIFT, pitchShiftAmount, 1+i*stepSize)
finish()