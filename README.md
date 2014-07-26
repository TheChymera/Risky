#Risk

Python functions with a convenient command line interface (`risky_cli.py`) to calculate the odds for single-attack battles in Risk-like games.

##Usage
From the containing folder:
```bash 
risky_cli.py [-h] [-f] [-d DICE_SIDES] attackers defenders
```

##Arguments

###Positional arguments:
  attackers             number of attacking units (integer 1 to 3)
  defenders             number of defending units (integer 1 to 2)

###Optional arguments:
  -h, --help            show this help message and exit
  -f, --force-lookup    force usage of the odds_lookup (non-formulaic, slow)
                        method
  -d DICE_SIDES, --dice-sides DICE_SIDES
                        specify the number of faces on the dice

Released under the GPLv3 license.
Project led by Horea Christian (address all e-mail correspondence to: h.chr@mail.ru)
