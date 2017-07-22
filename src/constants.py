
NUM_OF_SET_PER_QUAN = 4

WAIT_FOR_RIICHI_PAI = -1
END_RONG  = 1
END_LIUJU = 2

MONEY_START = 25000

MAX_WAIT_SEC = 4

SUOZI_NOMI = True
if SUOZI_NOMI:
    TILE_START = 30
else:
    TILE_START = 10
TILE_RANGE = 40 - TILE_START

DORA_DEFAULT = 5

MIN_TILES_IN_YAMA = 14
MAX_XUN = 18


#--------------- Graphics parameters ----------------#

WINDOW_WIDTH  = 1024
WINDOW_HEIGHT = 768
WINDOW_SIZE   = (WINDOW_WIDTH, WINDOW_HEIGHT)
MIDDLE_OF_WINDOW = (0.5 * WINDOW_WIDTH, 0.5 * WINDOW_HEIGHT)

# Tile size
TILE_FIGURE_SIZE = (128,128)
TILE_FIGURE_SIZEx, TILE_FIGURE_SIZEy = TILE_FIGURE_SIZE
TILE_FIGURE_BLANK_ON_BOTH_SIDES = 23
TILE_SIZE = (41, 64)
TILE_SIZEx, TILE_SIZEy = TILE_SIZE
# The blank part of the tile. This is used to make the drop clearer.
TILE_SIZE_BLANK = 9
TILE_INSIDE_TO_LEFT = 2
TILE_INSIDE_TO_BOTTOM = 2
TILE_INSIDE_POS = (TILE_INSIDE_TO_LEFT, TILE_INSIDE_TO_LEFT + TILE_SIZE_BLANK)
TILE_INSIDE_SIZE = (TILE_SIZEx - 2 * TILE_INSIDE_TO_LEFT, \
                    TILE_SIZEy - TILE_SIZE_BLANK - 2 * TILE_INSIDE_TO_BOTTOM)

# Tile size for dropped tiles, dora, other players hands.
TILE_SIZE_SMALL = (36, 56)
TILE_SIZE_SMALL_BLANK = 8

# Position of the table status
STAT_POS = (100,100)

# Position of the Yama
YAMA_POSx = MIDDLE_OF_WINDOW[0] - 4 * TILE_SIZE_SMALL[0]
YAMA_POSy = MIDDLE_OF_WINDOW[1] - TILE_SIZE_SMALL[1]

# Position of the analysis
ANALYSIS_POS = (500, 50)
ANALYSIS_POSx, ANALYSIS_POSy = ANALYSIS_POS


# Position of the end-of-game jiesuan
JIESUAN_POS = (500, 50)
JIESUAN_POSx, JIESUAN_POSy = JIESUAN_POS
JIESUAN_FONT = 24

# Position of player hand tiles
HAND_DIFF_TO_BOUNDARY = 40
HAND_POS_TO_BOTTOM = HAND_DIFF_TO_BOUNDARY + TILE_SIZEy
HAND_POS_TO_LEFT   = (WINDOW_WIDTH - 14* TILE_SIZEx) // 2

HAND_POSx, HAND_POSy = HAND_POS_TO_LEFT, WINDOW_HEIGHT - HAND_POS_TO_BOTTOM

# Size of the gap between hand and new tile
HAND_GAP = 8

# Size of difference in height between hand and chi,peng,gang etc.
HAND_CHI_PENG_GANG_DIFF = HAND_DIFF_TO_BOUNDARY //2

# Position used for showing ai hand tiles
# AI on the right. Position is the upleft corner of the very bottom handtile.
AI1_HAND_POSx = WINDOW_WIDTH - TILE_SIZE_SMALL[1] - HAND_DIFF_TO_BOUNDARY
AI1_HAND_POSy = (WINDOW_HEIGHT + 14* TILE_SIZE_SMALL[0]) // 2 - TILE_SIZE_SMALL[0]
# AI on the top. Position is the upleft corner of the very right handtile.
AI2_HAND_POSx = (WINDOW_WIDTH + 14 * TILE_SIZE_SMALL[0]) //2 - TILE_SIZE_SMALL[0]
AI2_HAND_POSy = HAND_DIFF_TO_BOUNDARY
# AI on the left. Position is the upleft corner of the very top handtile.
AI3_HAND_POSx = HAND_DIFF_TO_BOUNDARY
AI3_HAND_POSy = (WINDOW_HEIGHT - 14 * TILE_SIZE_SMALL[0]) //2


# Drops
MAX_DROP_A_LINE = 6
# Position of the dropped tiles of player
DROP_POS_GAP_TO_HAND = 40

DROP_POS_TO_BOTTOM = 3*(TILE_SIZEy-TILE_SIZE_BLANK) + TILE_SIZE_BLANK + HAND_POS_TO_BOTTOM + DROP_POS_GAP_TO_HAND
DROP_POS_TO_LEFT   = (WINDOW_WIDTH - MAX_DROP_A_LINE*TILE_SIZEx) //2
DROP_POSx, DROP_POSy = DROP_POS_TO_LEFT, WINDOW_HEIGHT - DROP_POS_TO_BOTTOM
# Position of the dropped tiles of AIs
AI1_DROP_POSx = WINDOW_WIDTH - HAND_DIFF_TO_BOUNDARY \
                             - TILE_SIZE_SMALL[1] * 4 \
                             + TILE_SIZE_SMALL_BLANK * 2 \
                             - DROP_POS_GAP_TO_HAND
AI1_DROP_POSy = (WINDOW_HEIGHT + MAX_DROP_A_LINE * TILE_SIZE_SMALL[0] )//2

AI2_DROP_POSx = (WINDOW_WIDTH + MAX_DROP_A_LINE * TILE_SIZE_SMALL[0] )//2 - TILE_SIZE_SMALL[0]
AI2_DROP_POSy =  HAND_DIFF_TO_BOUNDARY \
                + TILE_SIZE_SMALL[1] * 3 \
                - TILE_SIZE_SMALL_BLANK * 2 \
                + DROP_POS_GAP_TO_HAND

AI3_DROP_POSx =  HAND_DIFF_TO_BOUNDARY \
                + TILE_SIZE_SMALL[1] * 3 \
                - TILE_SIZE_SMALL_BLANK * 2 \
                + DROP_POS_GAP_TO_HAND
AI3_DROP_POSy = (WINDOW_HEIGHT - MAX_DROP_A_LINE * TILE_SIZE_SMALL[0]) //2

# Font sizes
FONT_SIZE = 24
FONT_SIZE_MENU = 32

# Menu position is determined by the fontsize of menu now.
MENU_POS = (HAND_POSx + FONT_SIZE_MENU/2 , HAND_POSy - FONT_SIZE_MENU + FONT_SIZE_MENU/2 )
MENU_POSx , MENU_POSy = MENU_POS
MENU_GAP = 2

# COLOR
WHITE = ( 255, 255, 255 )
BLACK = ( 0, 0, 0 )
GRAY  = ( 200, 200, 200 )
