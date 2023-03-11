import copy
def print_board(board):
    for line in board:
        print (line)
    print("_"*30)
def Check_Row(x,y,board,p):
    for i in range(9):
        if i!=x and board[y][i]!="x":
            p=p.replace(board[y][i],"")
    return p
def Check_Column(x,y,board,p):
    for i in range(9):
        if i!=y and board[i][x]!="x":
            p=p.replace(board[i][x],"")
    return p
def Check_Square(x,y,board,p):
    x1=x//3*3
    y1=y//3*3
    for x2 in range(3):
        for y2 in range(3):
            if x2!=x%3 and y2!=y%3 and board[y1+y2][x1+x2]!="x":
                p=p.replace(board[y1+y2][x1+x2],"")
    return p
def check_square_lines(board,x,y,num):
    x=x//3*3
    y=y//3*3
    x_locations=""
    y_locations=""
    for y1 in range(3):
        if num in board[y+y1][x] or num in board[y+y1][x+1] or num in board[y+y1][x+2]:
            x_locations=x_locations+str(y+y1)
    for x1 in range(3):
        if num in board[y][x+x1] or num in board[y+1][x+x1] or num in board[y+2][x+x1]:
            y_locations=y_locations+str(x+x1)
    if len(x_locations)!=1:
        x_locations="9"
    if len(y_locations)!=1:
        y_locations="9"
    return int(x_locations), int(y_locations)
def Set_P_Board(board):
    p_board=[["x","x","x","x","x","x","x","x","x"],["x","x","x","x","x","x","x","x","x"],["x","x","x","x","x","x","x","x","x"],["x","x","x","x","x","x","x","x","x"],["x","x","x","x","x","x","x","x","x"],["x","x","x","x","x","x","x","x","x"],["x","x","x","x","x","x","x","x","x"],["x","x","x","x","x","x","x","x","x"],["x","x","x","x","x","x","x","x","x"]]
    for x in range(9):
        for y in range(9):
            if(board[y][x]=="x"):
                p_board[y][x] = Check_Row(x,y,board,"123456789")
                p_board[y][x] = Check_Column(x,y,board,p_board[y][x])
                p_board[y][x] = Check_Square(x,y,board,p_board[y][x])
    for i in range(10):
        for x in range(3):
            for y in range(3):
                y1,x1=check_square_lines(p_board,x*3,y*3,str(i))
                if y1<9:
                    for a in range(9):
                        if a//3!=x:
                            p_board[y1][a]=p_board[y1][a].replace(str(i),"")
                if x1<9:
                    for a in range(9):
                        if a//3!=y:
                            p_board[a][x1]=p_board[a][x1].replace(str(i),"")

    return p_board
def Rewind(save_data,save_boards):
    i = len(save_data)-1
    board=copy.deepcopy(save_boards[i])
    save_data[i][3] = save_data[i][3]+1
    if save_data[i][3] != len(save_data[i][2]):
        board[save_data[i][1]][save_data[i][0]]==save_data[i][2][save_data[i][3]]
        return board,save_data,save_boards
    else:
        save_data.pop()
        save_boards.pop()
        return Rewind(save_data,save_boards)
def Ai(board,save_boards,save_data):
    p_board = Set_P_Board(board)
    for line in p_board:
        if "" in line:
            board,save_data,save_boards = Rewind(save_data,save_boards)
    p_board = Set_P_Board(board)
    board_backup = copy.deepcopy(board)
    for x in range(9):
        for y in range(9):
            if(len(p_board[y][x])==1 and  p_board[y][x]!="x"):
                board[y][x]=p_board[y][x]
            elif(p_board[y][x]!="x"):
                for letter in p_board[y][x]:
                    only=True
                    for x1 in range(9):
                        if x1!=x and letter in p_board[y][x1]:
                            only=False
                    if only:
                        board[y][x]=letter

                    only=True
                    for y1 in range(9):
                        if y1!=y and letter in p_board[y1][x]:
                            only=False
                    if only:
                        board[y][x]=letter

                    only=True
                    for x1 in range(3):
                        for y1 in range(3):
                            if not(x1==x%3 and y1==y%3) and letter in p_board[y1+y//3*3][x1+x//3*3]:
                                only=False
                    if only:
                        board[y][x]=letter
    
    if board_backup == board:
        save_boards.append(copy.deepcopy(board))
        found=False
        for x in range(9):
            for y in range(9):
                if board[y][x]=="x" and found==False:
                    save_data.append([x,y,p_board[y][x],0])
                    board[y][x] = p_board[y][x][0]
                    found=True
    return board
def Solved(board):
    for line in board:
        if "x" in line:
            return False
    return True
board=[["x","x","x","2","x","x","3","5","x"],
       ["8","x","3","1","x","x","x","x","x"],
       ["x","x","x","x","x","7","x","x","8"],
       ["x","x","2","x","4","x","x","7","x"],
       ["x","x","x","x","1","x","9","4","x"],
       ["5","9","x","x","x","x","8","x","x"],
       ["x","6","x","x","x","x","2","9","x"],
       ["x","4","x","6","x","x","x","x","x"],
       ["x","2","x","7","x","x","x","x","6"]]
save_boards = []
save_data = []
while Solved(board)==False:
    board=Ai(board,save_boards,save_data)
    print_board(board)
