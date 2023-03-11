import copy
def print_board(board):
    for line in board:
        print (line)
    print("_"*30)
def Overlap(str1,str2):
    overlap = ""
    for letter in str1:
        if letter in str2:
            overlap = overlap + letter
    return overlap
def Check_Row(board,x,y):
    possible="123456789"
    for x1 in range(9):
        if x1!=x and board[y][x1]!="x":
            possible = possible.replace(board[y][x1],"")
    return possible
def Check_Column(board,x,y):
    possible="123456789"
    for y1 in range(9):
        if y1!=y and board[y1][x]!="x":
            possible = possible.replace(board[y1][x],"")
    return possible
def Check_Square(board,x,y):
    possible="123456789"
    for x1 in range(3):
        for y1 in range(3):
            if x1!=x%3 and y1!=y%3 and board[y//3*3+y1][x//3*3+x1]!="x":
                possible = possible.replace(board[y//3*3+y1][x//3*3+x1],"")
    return possible
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
def Solved(board):
    for line in board:
        if "x" in line:
            return False
    return True
def Set_P_Board(board):
    p_board=[["x","x","x","x","x","x","x","x","x"],["x","x","x","x","x","x","x","x","x"],["x","x","x","x","x","x","x","x","x"],["x","x","x","x","x","x","x","x","x"],["x","x","x","x","x","x","x","x","x"],["x","x","x","x","x","x","x","x","x"],["x","x","x","x","x","x","x","x","x"],["x","x","x","x","x","x","x","x","x"],["x","x","x","x","x","x","x","x","x"]]
    for x in range(9):
        for y in range(9):
            if board[y][x]=="x":
                possible="123456789"
                possible = Overlap(possible,Check_Row(board,x,y))
                possible = Overlap(possible,Check_Column(board,x,y))
                possible = Overlap(possible,Check_Square(board,x,y))
                p_board[y][x] = possible
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
def Mistake(board):
    for line in board:
        if "" in line:
            return True
    return False
def Rewind(save_boards,save_data):
    i = len(save_boards)-1
    board = copy.deepcopy(save_boards[i])
    save_data[i][3] = save_data[i][3]+1
    if save_data[i][3] == len(save_data[i][2]):
        save_data.pop()
        save_boards.pop()
        return Rewind(save_boards,save_data)
    board[save_data[i][1]][save_data[i][0]] = save_data[i][2][save_data[i][3]]
    return board,save_boards,save_data
def Ai(board,save_boards,save_data):
    p_board = Set_P_Board(board)
    if Mistake(p_board):
        board,save_boards,save_data = Rewind(save_boards,save_data)
        p_board = Set_P_Board(board)
    board_backup = copy.deepcopy(board)
    for x in range(9):
        for y in range(9):
            if p_board[y][x]!="x" and len(p_board[y][x])==1:
                board[y][x] = p_board[y][x]
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
    if board == board_backup:
        save_boards.append(copy.deepcopy(board))
        found = False
        for x in range(9):
            for y in range(9):
                if found == False and p_board[y][x]!="x":
                    board[y][x] = p_board[y][x][0]
                    save_data.append([x,y,p_board[y][x],0])
                    found = True
    return board,save_boards,save_data
board=[['x', '7', 'x', '1', '6', 'x', '8', 'x', '4'], ['x', '9', '6', 'x', '4', '5', 'x', 'x', '1'], ['x', 'x', '8', 'x', 'x', '9', '3', 'x', 'x'], ['x', 'x', 'x', '2', 'x', '6', '9', '1', 'x'], ['2', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '8'], ['x', '6', '7', '3', 'x', '8', 'x', 'x', 'x'], ['x', 'x', '5', '6', 'x', 'x', '1', 'x', 'x'], ['7', 'x', 'x', '9', '1', 'x', '5', '2', 'x'], ['6', 'x', '1', 'x', '3', '2', 'x', '8', 'x']]
save_boards = []
save_data = []
while Solved(board)==False:
    board,save_boards,save_data=Ai(board,save_boards,save_data)
print_board(board) 