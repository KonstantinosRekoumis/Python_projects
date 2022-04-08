# ______________ EPIC CHESS SIMULATOR _____________________
# Developed by Konstantinos Rekoumis, April 2022
# GitHub: https://github.com/KonstantinosRekoumis
# An Object Oriented Alternative may follow
#__________________________________________________________
# A B C D E F G H
# 1 2 3 4 5 6 7 8
# These two arrays are treated as global scope constants that Define the chess board
import importlib.util as ul
_CLR_= False # enable or not the colors
skip_chr = 0
if ul.find_spec("colorama") is not None: #Check if colorama pack exists in the libraries if not stay simple
    # if you want the colored version simple open a Command Prompt and type :
    #  pip install colorama
    import colorama as clr
    clr.init()
    _CLR_ =True
    skip_chr = len(f"{clr.Fore.RED}")+len(f"{clr.Fore.WHITE}") #color shenanigans




hor_axis = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
ver_axis = [i for i in range(1,9)]

def move_diag(position, units,obstacles,obstacles_type):
    # Check the diagonal movement of each chess piece. Importing 
    # the piece's position and its units range.
    # To check whether a move is possible is checked whether it is within 
    # the board's bounds and whether is obstructed by another piece.
    # Namely when the collision target is the Color's king as it cannot be traded
    # the collision occurs one tile prior to the king's tile along the vector of attack.
    moves_d = []
    pos_x = position[0]
    pos_y = position[1]
    ind_x = hor_axis.index(pos_x)
    ind_y = ver_axis.index(pos_y)
    collision = [False,False,False,False] # Collision checking array. Initialized as False as no collisions where detected
    # Check whether an obstacle of type king exists and where is located on the obstacle's list.
    king_idx = 0
    king_ex = False
    if "king" in obstacles_type:
        king_idx = obstacles_type.index("king")
        king_ex = True
    #Collision is done by checking whether the movement coordinate is the same as an obstacle's.
    #Then if the obstacle is the color's king special rules apply in order to not trade the king.
    for i in range(1,units+1):
        #up-right movement
        if (ind_x+i<8) and (ind_y+i < 8) and not(collision[0]):
            moves_d.append((hor_axis[ind_x+i],ver_axis[ind_y+i]))
            if ((hor_axis[ind_x+i],ver_axis[ind_y+i]) in obstacles):
                if king_ex and (obstacles.index((hor_axis[ind_x+i],ver_axis[ind_y+i])) == king_idx):
                    moves_d.pop()
                collision[0] =True
        #down-right movement
        if (ind_x+i<8) and (ind_y-i >= 0) and not(collision[1]):
            moves_d.append((hor_axis[ind_x+i],ver_axis[ind_y-i]))
            if ((hor_axis[ind_x+i],ver_axis[ind_y-i]) in obstacles):
                if king_ex and (obstacles.index((hor_axis[ind_x+i],ver_axis[ind_y-i])) == king_idx):
                    moves_d.pop()
                collision[1] =True
        #up-left movement
        if (ind_x-i >= 0) and (ind_y+i < 8) and not(collision[2]):
            moves_d.append((hor_axis[ind_x-i],ver_axis[ind_y+i]))
            if ((hor_axis[ind_x-i],ver_axis[ind_y+i]) in obstacles):
                if king_ex and (obstacles.index((hor_axis[ind_x-i],ver_axis[ind_y+i])) == king_idx):
                    moves_d.pop()
                collision[2] =True
        #down-left movement
        if (ind_x-i >= 0) and (ind_y-i >= 0) and not(collision[3]):
            moves_d.append((hor_axis[ind_x-i],ver_axis[ind_y-i]))
            if ((hor_axis[ind_x-i],ver_axis[ind_y-i]) in obstacles):
                if king_ex and (obstacles.index((hor_axis[ind_x-i],ver_axis[ind_y-i])) == king_idx):
                    moves_d.pop()
                collision[3] =True
        
    return moves_d

def move_nominal(position, units,obstacles,obstacles_type):
    # Similar to the diagonal movement we check collisions here too. 
    # The movements list are generated in a similar fashion.
    moves_v = []
    moves_h = []
    pos_x = position[0]
    pos_y = position[1]
    ind_x = hor_axis.index(pos_x)
    ind_y = ver_axis.index(pos_y)
    collision = [False,False,False,False]
    king_idx = 0
    king_ex = False
    if "king" in obstacles_type:
        king_idx = obstacles_type.index("king")
        king_ex = True
    
    for i in range(1,units+1):
        #right
        if (ind_x+i<8) and not(collision[0]):
            moves_h.append((hor_axis[ind_x+i],pos_y))
            if ((hor_axis[ind_x+i],pos_y) in obstacles):
                if king_ex and (obstacles.index((hor_axis[ind_x+i],pos_y)) == king_idx):
                    moves_h.pop()
                collision[0] =True
        # left
        if (ind_x-i >= 0) and not(collision[1]):
            moves_h.append((hor_axis[ind_x-i],pos_y))
            if ((hor_axis[ind_x-i],pos_y) in obstacles):
                if king_ex and (obstacles.index((hor_axis[ind_x-i],pos_y)) == king_idx):
                    moves_h.pop()
                collision[1] =True
        # up
        if (ind_y+i<8) and not(collision[2]):
            moves_v.append((pos_x,ver_axis[ind_y+i]))
            if ((pos_x,ver_axis[ind_y+i]) in obstacles):
                if king_ex and (obstacles.index((pos_x,ver_axis[ind_y+i])) == king_idx):
                    moves_h.pop()
                collision[2] =True
        # down
        if (ind_y-i >= 0) and not(collision[3]):
            moves_v.append((pos_x,ver_axis[ind_y-i]))
            if ((pos_x,ver_axis[ind_y-i]) in obstacles):
                if king_ex and (obstacles.index((pos_x,ver_axis[ind_y-i])) == king_idx):
                    moves_h.pop()
                collision[3] =True
    
    return moves_h,moves_v

def movement(position,move_units,obstacles,obstacles_type):
    # A neat routine to concatenate the movement functions
    moves_h, moves_v = move_nominal(position,units = move_units,obstacles=obstacles, obstacles_type = obstacles_type)
    moves_d = move_diag(position,units = move_units,obstacles=obstacles, obstacles_type = obstacles_type)

    sum = []
    for i in moves_d:
            sum.append(i)
    for i in moves_h:
            sum.append(i)
    for i in moves_v:
            sum.append(i)

    return sum, moves_d, moves_h, moves_v
def key_to_sort(t):
    #expect a tuple of form ("K",("X",y))
    return t[1]

def print_brd(pieces,moves):
    # A Command Line Renderer which plots the board with the pieces and the possible moves
    board = "   "
    
    #    | A | B | C | D | E | F | G | H |
    # ---+---+---+---+---+---+---+---+---+---
    for i in hor_axis:
        board += f"| {i} "
    board += "|\n---"+"+---"*9+"\n"

    # to render the board properly we must rid of the moves where
    targets = pieces
    for i in moves:
        append = True
        for j in pieces:
            if i[1] == j[1]:
                if _CLR_:
                    targets[targets.index(j)] = (clr.Fore.RED+targets[targets.index(j)][0]+clr.Fore.WHITE ,targets[targets.index(j)][1])
                append = False
                break
        if append:
            targets.append(i)

    targets.sort(key = key_to_sort)

    for i in range(8):
        board += f" {ver_axis[-i-1]} "
        row = ""    
        skip_ = 0    
        for j in range(len(targets)):
            if targets[j][1][1] == ver_axis[-i-1]:
                row += "|   "*int(hor_axis.index(targets[j][1][0])-len(row)/4)+f"| {targets[j][0]} "
                # print(targets[j])
                if _CLR_ and len(targets[j][0])>1:
                    skip_ +=1
        if len(row) <32:
            row += "|   "*(8-int((len(row)-skip_*skip_chr)/4))
        row += f"| {ver_axis[-i-1]}"
        board += row+"\n---"+"+---"*9+"\n"
    board += "   "
    for i in hor_axis:
        board += f"| {i} "
    print()
    print(board+"|")

def main():
    print("#"*15)
    print("Epic Chess Simulator")
    print("Considering that the Black King, White King, and White Queen are only left standing, and it is the Blacks' turn\n we calculate where the Black King is threatened. To do so you need to input each piece's table\n coordinates at the following format \"A 1\" (The Characters are expected in ASCII format)")
    queen=input("Give the Queen's coordinates: ").split(' ')
    wking=input("Give the White King's coordinates: ").split(' ')
    bking=input("Give the Black King's coordinates: ").split(' ')
    print("#"*15)
    # %%%%% DEBUG ONLY %%%%%
    # It 's tiresome to enter all the values manually each time 
    # queen = ("H",7)
    # wking = ("A",1)
    # bking = ("A",2)
    # %%%%%%%%%%%%%%%%%%%%%%% 

    queen = (queen[0],int(queen[1]))
    wking = (wking[0],int(wking[1]))
    bking = (bking[0],int(bking[1]))


    mv_queen = movement(queen,8,[wking],["king"])[0]
    mv_wking = movement(wking,1,[queen],["queen"])[0]
    mv_bking = movement(bking,1,[],[])[0]

    #Check if movements are available for the Black King 
    # Saving them differently for White queen and White King is utilized later 
    # to implement some "MEME" moves
    q_check = []
    for i in mv_queen:
        if i in mv_bking:
            q_check.append(i)

    k_check = []
    for i in mv_wking:
        if i in mv_bking:
            k_check.append(i)

    #Checks if the black king can defeat the other king or queen and if it's safe to do so
    m = 0
    moves = []
    slayer = False # Pretty MEME Scenarios but oh well ¯\_(ツ)_/¯ ¯\_(ツ)_/¯
    for i in mv_bking:
        #Checking the Black King's Moves
        if (i in k_check) or (i in q_check):
            m += 1
        else:
            moves.append(i)
        if not(i in q_check) and not(i in k_check) and (i == queen):
            print(f"The Black King can defeat the White Queen and is safe to do so. Move him to : {i[0]} {i[1]}" )
            slayer = True
        if not(i in q_check) and not(i in k_check) and (i == wking):
            print(f"The Black King can defeat the White King and is safe to do so. Move him to : {i[0]} {i[1]}" )
            slayer = True
    if (bking in mv_queen) or (bking in mv_wking) or len(moves) == 0:    
        if (m == len(mv_bking) or len(moves) == 0 ) and not(slayer):
            print("Roi Mat. The Black King is Doomed.")
        elif m <= len(mv_bking):
            print("Roi. The Black King can still Survive. He can move to :")
            for i in moves:
                print(i[0]," ",i[1])
    else:
        print("The Black King is safe at the moment. He can move to :")
        for i in moves:
            print(i[0]," ",i[1])


    print_brd([("♕",queen),("♔",wking),("♚",bking)],[("X",i) for i in moves])


try:
    main()
except KeyboardInterrupt:
    print("\nSad Times. We 'll never know what became of the Black King")
