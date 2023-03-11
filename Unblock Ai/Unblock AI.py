import copy
def move_iterate(past_boards,pieces):
    #print_past_boards(past_boards)
    board=past_boards[len(past_boards)-1]
    #for line in board:
    #    print(line)
    #print("___________________")
    if check_win(board):
        return True,past_boards
    
    if duplicate_move_check(past_boards):
        #print("WWWWWWWWWWWWWWWWWWWWWWWWWW")
        return False,past_boards
    
    moves=find_moves(board,pieces)
    #print(moves,"RRRRRRRRRRRR")
    for move in moves:
        #print(move,"EEEE",pieces)
        pieces1=play_move(move,copy.deepcopy(pieces))
        past_boards_1=copy.deepcopy(past_boards)
        past_boards_1.append(draw_board(pieces1))
        #print(pieces)
        state,past_boards_1=move_iterate(past_boards_1,pieces1)
        if state:
            return state,past_boards_1
    return True,["fail"]
def print_past_boards(past_boards):
    for board in past_boards:
        for line in board:
            print(line)
        print("__________")
def duplicate_move_check(past_boards):
    for i in range(len(past_boards)):
        if past_boards.count(past_boards[i])>1:
            return True
    return False

def check_win(board):
    if board[2][4]=="0" and board[2][5]=="0":
        return True
    return False
    
def find_moves(board,pieces):
    moves=[]
    for a in range(len(pieces)):
        piece=pieces[a]
        i=1
        y=piece[1]-piece[3]*i
        x=piece[0]-piece[2]*i
        while y>=0 and y<6 and x>=0 and x<6 and board[y][x]=="":
            moves.append([a,-i])
            i=i+1
            y=piece[1]-piece[3]*i
            x=piece[0]-piece[2]*i
            
        i=1
        y=piece[1]+piece[3]*(i+piece[4]-1)
        x=piece[0]+piece[2]*(i+piece[4]-1)
        while y>=0 and y<6 and x>=0 and x<6 and board[y][x]=="":
            moves.append([a,i])
            i=i+1
            y=piece[1]+piece[3]*(i+piece[4]-1)
            x=piece[0]+piece[2]*(i+piece[4]-1)
    return moves
            
def play_move(move,pieces):
    pieces[move[0]][0]=pieces[move[0]][0]+pieces[move[0]][2]*move[1]
    pieces[move[0]][1]=pieces[move[0]][1]+pieces[move[0]][3]*move[1]
    return pieces
        

def draw_board(pieces):
    board=[["","","","","",""],
       ["","","","","",""],
       ["","","","","",""],
       ["","","","","",""],
       ["","","","","",""],
       ["","","","","",""]]
    for a in range(len(pieces)):
        piece=pieces[a]
        for i in range(piece[4]):
            board[piece[1]+piece[3]*i][piece[0]+piece[2]*i]=str(a)
    return board
    
board=[["","","","","",""],
       ["","","","","",""],
       ["","","","","",""],
       ["","","","","",""],
       ["","","","","",""],
       ["","","","","",""]]
      
pieces=[[0,2,1,0,2],[0,0,0,1,2],[1,0,1,0,3],[1,1,1,0,3],[2,2,0,1,2],[3,2,0,1,2],[0,3,1,0,2],[4,1,0,1,3],[5,1,0,1,3],[1,5,1,0,2],[3,4,0,1,2],[4,4,1,0,2]]#x,y,direction(x,y),length
for line in draw_board(pieces):
    print(line)
check,past_boards=move_iterate([draw_board(pieces)],pieces)
print("+++++++++++++++++++++++++++++++")
print_past_boards(past_boards)
