# Description: This file contains all the constants used in the game.

class Constants:
    FAIL = 0
    SUCCESS = 1
    INITIAL_ESTIMATED_SIZE = 21
    AGENT = 69
    ENCODING = "utf-8"
    INITIAL_VIEW_RANGE = 3
    ADDR = ('127.0.0.1', 8080)
    MAX_COLOR_VALUE = 256
    MAX_SERVER_RESPONSE_SIZE = 4096 * 4
    
    WALL = 0
    PATH = 255
    ENTRANCE = 64
    EXIT = 182
    XRAY_INCREMENT = 16
    FOG_TILE = 32
    TOWER_TILE = 224

    TRAP_MOVEMENT_TILE = [96, 97, 98, 99, 100]
    TRAP_REWIND_TILE = [101, 102, 103, 104, 105]
    TRAP_PUSHFORWARD_TILE = [106, 107, 108, 109, 110]
    TRAP_PUSHBACK_TILE = [111, 112, 113, 114, 115]

    PORTAL_IDS = [
        150, 151, 152, 153, 154, 155, 156, 157, 158, 159,
        160, 161, 162, 163, 164, 165, 166, 167, 168, 169
    ]