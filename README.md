#Risky

Python functions with a convenient command line interface (`risky_cli.py`) to calculate the odds for single-attack battles in Risk-like games.
The function lets you specify many variations including number of attacking units, defending units, and even dice sides.
We use either formulaic odds calculation or explicit lookup from tables of all outcome possibilities (the latter being significantly slower for large dice side numbers).

A more in-depth explanation of the formulas, as well as reference odds tables for popular game configurations can be found in the script's [tutorial page](http://chymeric.eu/blog/2014/07/23/per-attack-risk-dice-odds/). 

##Usage
From the containing folder:
```
python risky_cli.py [-h] [-f] [-d DICE_SIDES] attackers defenders
```

Example (7-sided dice, 4 attacking dice are rolled against 1 defending dice):
```
python risky_cli.py -d 7 4 1
```

##Arguments

```
positional arguments:
  attackers             number of attacking units (integer 1 to 3)
  defenders             number of defending units (integer 1 to 2)

optional arguments:
  -h, --help            show this help message and exit
  -f, --force-lookup    force usage of the odds_lookup (non-formulaic, slow)
                        method
  -d DICE_SIDES, --dice-sides DICE_SIDES
                        specify the number of faces on the dice
```

Released under the GPLv3 license.
Project led by Horea Christian (address all e-mail correspondence to: h.chr@mail.ru)
