#!/usr/bin/python
__author__ = 'Horea Christian'
import argparse
import one_attack

parser = argparse.ArgumentParser()
parser.add_argument("attackers", help="number of attacking units (integer 1 to 3)", type=int)
parser.add_argument("defenders", help="number of defending units (integer 1 to 2)", type=int)
parser.add_argument("-f", "--force-lookup", help="force usage of the odds_lookup (non-formulaic, slow) method", action="store_true")
parser.add_argument("-d", "--dice-sides", help="specify the number of faces on the dice", default=6, type=int)
args = parser.parse_args()

if str(args.dice_sides)[0] == 8:
    n = "n"
elif args.dice_sides == 11:
    n = "n"
else:
    n = ""

if args.attackers >= 2:
    attackers_s="s"
else:
    attackers_s=""
if args.defenders >= 2:
    defenders_s="s"
else:
    defenders_s=""

print"Using a"+n+" "+str(args.dice_sides)+"-sided dice and "+str(args.attackers)+" attacker"+attackers_s+" and "+str(args.defenders)+" defender"+defenders_s+", your outcome odds are:"

if args.force_lookup:
    victory, tie, defeat, units_lost = one_attack.odds_lookup(args.attackers, args.defenders, dice_sides=args.dice_sides)
    print "Victory =",victory
    print "    Tie =",tie
    print " Defeat =",defeat
    print "\n Your expected unit attrition is",units_lost,"for every 1 unit lost by the defender."

else:
    victory, tie, defeat, units_lost = one_attack.odds_formulae(args.attackers, args.defenders, dice_sides=args.dice_sides)
    print "Victory =",victory
    print "    Tie =",tie
    print " Defeat =",defeat
    print "\n Your expected unit attrition is",units_lost,"for every 1 unit lost by the defender."
