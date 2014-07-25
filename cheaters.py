########################################################################################################
# cheaters.py
#    by Red_Cyberdragon
# Debugging script for Bigger is Better (ZillaRL).
# http://www.forcastia.com | http://gaingirls.tumblr.com
#    Last updated on July 24, 2014
#    Unofficial Addition
#
# USE: To facilitate testing of the game through the use of direct variable manipulation at runtime
########################################################################################################
# Notes:
#
#	This file is kept separate to allow the quick and easy removal of debug capabilities at
# release. Even if this is not to be removed, it helps to organize the file in a way we can track.
#
# in zillarldata.py
#      - all debug options should be at the top of the file and the variables all clearly labeled
#        with DEBUG_ prefix.
#
# in zillarl.py
#      - in handleKeys()
#		- At the end of the if statements, the debug menu's toggle key.
#      - in <GAME_RENDERER>
#		- Shows custom built menu with list of variables and 'selector'

import libtcodpy as libtcod


