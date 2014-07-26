from __future__ import division
__author__ = 'Horea Christian'

import numpy as np
from itertools import product

def odds_formulae(attackers, defenders, dice_sides=6, victory=0, tie=0, defeat=0):
    if attackers == 1 and defenders == 2:
	for n in np.arange(dice_sides)+1:
	    victory += (n-1)*(dice_sides**attackers-n**attackers)/dice_sides**(attackers+defenders)
	    for m in np.arange(dice_sides-n+1)+n:
		victory += (dice_sides**attackers-m**attackers)/dice_sides**(attackers+defenders)
	defeat = 1 - victory
    #~ elif attackers == 2 and defenders == 2:
	#~ for (n,m) in product(np.arange(dice_sides)+1, np.arange(dice_sides)+1):
		#~ victory += (dice_sides-n)*(dice_sides-m)/dice_sides**4
	#~ defeat = 1 - victory
    elif defenders == 1:
	for n in np.arange(dice_sides)+1:
	    victory += (dice_sides**attackers-n**attackers)/dice_sides**(attackers+defenders)
	defeat = 1 - victory
    else:
	print "Automatically switching to lookup-method to determine odds as your specified attacker and defender values have no corresponding odds formula."
	victory, tie, defeat = odds_lookup(attackers, defenders, dice_sides, victory, tie, defeat)
    
    return victory, tie, defeat
    
def odds_lookup(attackers, defenders, dice_sides=6, victory=0, tie=0, defeat=0):
    # The function has only been tested for attackers in (1,2,3) and defenders in (1,2).
    
    from itertools import product
    fighting_units = min(attackers,defenders)
    for sequence in np.array(list(product(np.arange(dice_sides)+1, repeat=(attackers+defenders)))):
	#sort values ascendingly (for attackers) and descendingly (for defenders)
	sequence = np.concatenate((np.sort(sequence[:attackers])[::-1],np.sort(sequence[-defenders:])))
	score = 0
	for a in np.arange(fighting_units):
	    if sequence[a] > sequence[-(a+1)]:
		score += 1
	if score >= fighting_units:
	    victory += 1
	elif score == 0:
	    tie += 1
	else:
	    defeat += 1
	    	    
    victory = victory/dice_sides**(attackers+defenders)
    defeat = defeat/dice_sides**(attackers+defenders)
    tie = tie/dice_sides**(attackers+defenders)
    
    if victory+tie+defeat != 1.0:
	raise ValueError("The sum of probabilities does not equal 1. Please ceheck your input and that the function supports it.")
    
    return victory, tie, defeat

