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

