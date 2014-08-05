############################################################
# ZillaRL - Main.py
#-----------------------------------------------------------
# Project by: BlueyDragon
# Script by : Red_Cyberdragon
# Copyright (c) 2014 
#-----------------------------------------------------------
# Main python script file used for organizing program flow
############################################################

# Include all sources
import zillarl as gameLogic


#########################################################################################################
#Initialize the consoles, font style, and FPS limit.
gameLogic.libtcod.console_set_custom_font('terminal8x8_gs_tc.png', gameLogic.libtcod.FONT_TYPE_GREYSCALE | gameLogic.libtcod.FONT_LAYOUT_TCOD)
gameLogic.libtcod.console_init_root(gameLogic.data.SCREEN_WIDTH, gameLogic.data.SCREEN_HEIGHT, "ZillaRL", False)
gameLogic.libtcod.sys_set_fps(gameLogic.data.FPS_LIMIT)

con = gameLogic.libtcod.console_new(gameLogic.data.MAP_WIDTH, gameLogic.data.MAP_HEIGHT)
msgPanel = gameLogic.libtcod.console_new(gameLogic.data.MESSAGE_PANEL_WIDTH, gameLogic.data.MESSAGE_PANEL_HEIGHT)
sidebar = gameLogic.libtcod.console_new(gameLogic.data.SIDEBAR_WIDTH, gameLogic.data.SIDEBAR_HEIGHT)
infoPanel = gameLogic.libtcod.console_new(gameLogic.data.MAP_WIDTH / 2, gameLogic.data.MAP_HEIGHT)

#########################################################################################################
# Launch Game
gameLogic.mainMenu()
