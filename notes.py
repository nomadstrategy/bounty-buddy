"""
test calculations and features of the bounty calculator and use cases

User Story: 
user should be able to call tournaments as easily as possible.

#1. Users should be able to create a custom tournament
    *factory function for classes?
    # buyin, starting stack different for each tournament
    # knockout type, value might be consistent between all types 
    # tournament = knockout(bounty_value=0.4, starting_bounty=0.5, bounty_earned=0.5)

#2. Users should be able to easily get bounty conversions
    
    #   $10 Bounty Tournament starting with:
        10000 chips/ $4.9 KO -->
        10000 initial bounty chipvalue
        ... enter new bounty to get an updated chipvalue (or q, h, n): --> ...
    #

#3. Users should be able to continue working on a tournament until finished
    # while True... break on 'q'

#4  easy to understand syntax. 
# mtt = pko(10,3000) --> progressive knockout with 10 bi, 3000 starting chips
# mtt.calc(30) --> displays pko(10,3000).calc(30) or as needed (30 displayed bounty)

#5 pot-odds including adjusted bounty chipvalue
"""


# generate classes like:

# Headhunter = Progressive('buyin'=10,'ko_rate'=0.75, 'starting_stack=10000)

# mtt = Headhunter()
# mtt --> (print info on mtt)
#
# mtt.calc_bounty(33.65)
# --> display parameters then answers seperately , clearly
#
#
#
# !bounty
#
# -> enter in tournament type:
#                               # ko_rate is % awarded for knockout
#
#      1. SaturdayProgressive('buyin'=10,'ko_rate'=0.75, 'starting_stack=10000)
#      2. ProgressiveKnockout('buyin'=10, 'ko_rate'=0.5, 'starting_stack=5000')
#      3. FlatBounty('buyin_dollars'=5.5, 'ko_dollars'=1.25, 'starting_stack=3000')
#      4. etc...
#      5. or enter the number 5 to build and save a new structure
#      6. type 'Q' to quit, or 'H' for help, or 'A' for advanced commands
#
#

#
#
#               !TODO: CONSOLE OUTPUT
#
#
# #What is opponents bounty? : $4.9
# DEBUG:root:$4.9 bounty displayed
# DEBUG:root:4000.0 chipvalue with these parameters:
# ProgressiveKO(buyin=10, starting_stack=10000, bounty=4.9, knockout_rate=0.4)
#
#
#

