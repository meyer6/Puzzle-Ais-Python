import copy
def check_column(board,x):
    nums=""
    for y in range(9):
        if board[y][x]!="x":
            nums=nums+board[y][x]
    return nums

def check_row(board,y):
    nums=""
    for x in range(9):
        if board[y][x]!="x":
            nums=nums+board[y][x]
    return nums

def check_square(board,x,y):
    nums=""
    for y1 in range(3):
        for x1 in range(3):
            if board[(y//3)*3+y1][(x//3)*3+x1]!="x":
                nums=nums+board[(y//3)*3+y1][(x//3)*3+x1]
    return nums

def delete_duplicates(str1,str2):
    for letter in str1:
        if letter in str2:
            str2=str2.replace(letter,"")
    return str2

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
        
    
def set_board2(board):
    board2=[["123456789","123456789","123456789","123456789","123456789","123456789","123456789","123456789","123456789"],
       ["123456789","123456789","123456789","123456789","123456789","123456789","123456789","123456789","123456789"],
       ["123456789","123456789","123456789","123456789","123456789","123456789","123456789","123456789","123456789"],
       ["123456789","123456789","123456789","123456789","123456789","123456789","123456789","123456789","123456789"],
       ["123456789","123456789","123456789","123456789","123456789","123456789","123456789","123456789","123456789"],
       ["123456789","123456789","123456789","123456789","123456789","123456789","123456789","123456789","123456789"],
       ["123456789","123456789","123456789","123456789","123456789","123456789","123456789","123456789","123456789"],
       ["123456789","123456789","123456789","123456789","123456789","123456789","123456789","123456789","123456789"],
       ["123456789","123456789","123456789","123456789","123456789","123456789","123456789","123456789","123456789"]]
    for x in range(9):
        for y in range(9):
            if board[y][x]!="x":
                board2[y][x]="x"
            else:
                board2[y][x]=delete_duplicates(check_column(board,x),board2[y][x])
                board2[y][x]=delete_duplicates(check_row(board,y),board2[y][x])
                board2[y][x]=delete_duplicates(check_square(board,x,y),board2[y][x])
    for i in range(10):
        for x in range(3):
            for y in range(3):
                y1,x1=check_square_lines(board2,x*3,y*3,str(i))
                if y1<9:
                    for a in range(9):
                        if a//3!=x:
                            board2[y1][a]=board2[y1][a].replace(str(i),"")
                if x1<9:
                    for a in range(9):
                        if a//3!=y:
                            board2[a][x1]=board2[a][x1].replace(str(i),"")
    return board2

def solve_ones(board,board2):
    for x in range(9):
        for y in range(9):
            if board2[y][x]!="x" and len(board2)==1:
                board[y][x]=board2[y][x]
    return board

def solve_squares(board,board2):
    for x1 in range(3):
        for y1 in range(3):
            nums=check_square(board2,x1*3,y1*3)
            for a in range(10):
                if nums.count(str(a))==1:
                    for x in range(3):
                        for y in range(3):
                            if str(a) in board2[y1*3+y][x1*3+x]:
                                board[y1*3+y][x1*3+x]=str(a)
    return board
    
def check_solved(board):
    for line in board:
        if "x" in line:
            return False
    return True

def mistake_check(board2):
    for x in range(9):
        for y in range(9):
            if board2[y][x]=="":
                return True
    return False

def guess(board,mistake_index):
    board2=set_board2(board)
    for x in range(9):
        for y in range(9):
            if board2[y][x]!="x":
                board[y][x]=board2[y][x][mistake_index]
                num=board2[y][x][mistake_index]
                return board,num

def validate_guess(board,board2,save_board,mistake_index):
    l=len(mistake_index)-1
    mistake_index[l][0]=mistake_index[l][0]+1
    if mistake_index[l][0]>=mistake_index[l][1]:
        mistake_index.pop()
        save_board.pop()
        board=copy.deepcopy(save_board[len(save_board)-1])
        return validate_guess(board,board2,save_board,mistake_index)
    else:
        board,num=guess(board,mistake_index[l][0])
        return board,board2,save_board,mistake_index
    
def print_board(board):
    for line in board:
        print (line)
    print("_"*30)
board=[["x","x","x","x","x","x","x","x","x"],
       ["x","x","x","x","x","x","x","x","x"],
       ["x","x","x","x","x","x","x","x","x"],
       ["x","x","x","x","x","x","x","x","x"],
       ["x","x","x","x","x","x","x","x","x"],
       ["x","x","x","x","x","x","x","x","x"],
       ["x","x","x","x","x","x","x","x","x"],
       ["x","x","x","x","x","x","x","x","x"],
       ["x","x","x","x","x","x","x","x","x"]]
mistake_index=[]
save_board=[]

while check_solved(board)==False:
    print_board(board)
    board2=set_board2(board)
    if mistake_check(board2):
        for line in save_board:
            print_board(line)
            print("::::::::::::::::::::::::")
        board=copy.deepcopy(save_board[len(save_board)-1])
        board,board2,save_board,mistake_index=validate_guess(board,board2,save_board,mistake_index)
            
    old_board=copy.deepcopy(board)
    
    board2=set_board2(board)
    board=solve_ones(board,board2)
    
    board2=set_board2(board)
    board=solve_squares(board,board2)

    if old_board==board:
        print("WWWWWWWWWWWWWWWWWWWWWWWWWWWW")
        save_board.append(copy.deepcopy(board))
        board,num=guess(board,0)
        mistake_index.append([0,int(num)])

        
for line in board:
    print (line)
#for line in board2:
#   print (line)
