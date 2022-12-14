import sys
from os.path import abspath, dirname, join

# Sets path to the app's main folder
if __name__ == "__main__":
    sys.path.insert(0, abspath(join(dirname(__file__), '../..')))

from scripts.libs import *

#TODO:
#* Pawn
#* Knight
#* Bishop
#* Rook
#* Queen
#* King
#♟♞♝♜♛♚♙♘♗♖♕♔

WHITE = X0.WHITE
BLACK = X0.neNOIR

class Style:
    unicodes = {
        'Empty' : '•',
        'Pawn'  : '♙',
        'Knight': '♞',
        'Bishop': '♝',
        'Rook'  : '♜',
        'Queen' : '♛',
        'King'  : '♚'
    }

    initials = {
        'Empty' : '#',
        'Pawn'  : 'P',
        'Knight': 'N',
        'Bishop': 'B',
        'Rook'  : 'R',
        'Queen' : 'Q',
        'King'  : 'K'
    }

MOVES = {
    'Empty' : None,

    'Pawn'  : lambda pos1, pos2, face:
    pos2[1] - pos1[1] <= face and pos1[0] == pos2[0],

    'Knight': lambda pos1, pos2      :
    abs(pos1[0] - pos2[0]) in (1,2) and abs(pos1[1] - pos2[1]) in (1,2),

    'Bishop': lambda pos1, pos2      :
    abs(pos2[0] - pos1[0]) == abs(pos2[1] - pos1[1]),

    'Rook'  : lambda pos1, pos2      :
    pos1[0] == pos2[0] or pos1[1] == pos2[1],

    'Queen' : lambda pos1, pos2      :
    MOVES.Bishop(pos1, pos2) or MOVES.Rook(pos1, pos2),

    'King'  : lambda pos1, pos2      :
    ((pos1[0]-pos2[0])**2 + ( pos1[1]-pos2[1])**2)**0.5 <= 2**0.5
}

Pieces:list = []
Whites:list = []
Blacks:list = []
W_TILE:str  = WHITE + Style.unicodes['Empty'] + C0.END
B_TILE:str  = BLACK + Style.unicodes['Empty'] + C0.END

# Defining Pieces Class:
class Piece:

    def __init__(this, name:str, team:str, style = Style.unicodes) -> None:

        if name == team == None:
            this.space   = True
            this.__str__ = lambda: ''
            return

        this.name   = name
        this.move   = MOVES[name]
        this.team   = team
        this.style  = style
        this.sprite = C0.BOLD + team + style[name] + C0.END

        if team == BLACK: Blacks.append(this)
        if team == WHITE: Whites.append(this)
        if True         : Pieces.append(this)

    def location(this):
        pass

    def highlight(this, color):

        if color == None:
            color = ''

        this.sprite = C0.BOLD + color + this.team + this.style[this.name] + C0.END

    def color(this, color):

        if color == None:
            color = ''

        this.sprite = C0.BOLD + this.team + color + this.style[this.name] + C0.END

_EMPTY:Piece = Piece(None, None)

# Defining Table Class:
class Table:

    def __init__(this, size:int = 8, style:Style = Style.unicodes) -> None:
        this.size  = size
        this.style = style

        this.board = [
                        [
                    (W_TILE if (_1+_2) % 2 else B_TILE) for _2 in range(size)
                        ] for _1 in range(size)
                     ]

        this.setup = [[_EMPTY for _ in range(size)] for _ in range(size)]
        this.setBoard()

    def spot(this, X, Y):
        _x = X
        _y = (this.size - Y -1) % this.size

        return this.setup[_y][_x]


    def setBoard(this):

        MAP = this.setup

        for x in range(this.size):
                MAP[x][1] = Piece('Pawn', BLACK, Style.initials)


    def move(this, pos1:tuple, pos2:tuple):
        x1, y1 = pos1
        x2, y2 = pos2

        this.setup[x2][y2] = this.setup[x1][y1]
        this.setup[x1][y1] = 0

    def print(this):

        for y in range(this.size):
            for x in range(this.size):
                _y = y
                y = (this.size - y - 1) % this.size


                if this.setup[x][y] != _EMPTY:
                    spot = this.setup[x][y].sprite
                else:
                    spot = this.board[x][y]
                y = _y
                print(spot, end=' ')
            print()
        print()


if __name__ == "__main__":

    clear()
    table = Table(style = Style.initials)

    table.setup[1][1].color(X0.RED)
    table.print()

    table.setup[1][1].color(None)
    table.print()

    print()
    enterContinue(Clear = 0)
