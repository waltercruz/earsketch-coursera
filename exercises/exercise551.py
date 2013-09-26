#
#
#       script_name: exercise 551
#
#       author: Walter Cruz
#
#       description: A simple house beat.
#
#
#

from earsketch import *


init()
setTempo(120)

for i in range(1,5):
	makeBeat(OS_KICK06, 1, i, '0---0---0---0---')
	makeBeat(OS_CLOSEDHAT03,2,i,'0---0---0---0---')
	makeBeat(OS_CLOSEDHAT06,3,i,'-000-000-000-000')	
	makeBeat(OS_CLAP01,4,i,'----0-------0---')

finish()
