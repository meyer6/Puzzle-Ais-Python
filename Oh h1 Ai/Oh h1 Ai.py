import copy
def AI(board):
    for y in range(len(board)):
        for x in range(len(board[y])-1):
            if board[y][x] == board[y][x+1] and board[y][x] != 2:
                if x - 1 >= 0:
                    board[y][x-1] = (board[y][x] + 1) % 2
                if x + 2 < len(board[y]):
                    board[y][x+2] = (board[y][x] + 1) % 2
        for x in range(len(board[y])-2):
            if board[y][x] == board[y][x+2] and board[y][x] != 2:
                board[y][x+1] = (board[y][x] + 1) % 2
        for i in range(2):
            if board[y].count(i) == len(board[y])//2:
                for x in range(len(board[y])):
                    if board[y][x] == 2:
                        board[y][x] = (i + 1) % 2
    for x in range(len(board)):
        for y in range(len(board)-1):
            if board[y][x] == board[y+1][x] and board[y][x] != 2:
                if y - 1 >= 0:
                    board[y-1][x] = (board[y][x] + 1) % 2
                if y + 2 < len(board[y]):
                    board[y+2][x] = (board[y][x] + 1) % 2
        for y in range(len(board)-2):
            if board[y][x] == board[y+2][x] and board[y][x] != 2:
                board[y+1][x] = (board[y][x] + 1) % 2
        for i in range(2):
            column = []
            for y in range(len(board)):
                column.append(board[y][x])
            if column.count(i) == len(column)//2:
                for y in range(len(board)):
                    if board[y][x] == 2:
                        board[y][x] = (i + 1) % 2
    return board
def Mistake(board):
    for y in range(len(board)):
        for x in range(len(board[y])-2):
            if board[y][x] == board[y][x+1] and board[y][x] == board[y][x+2]  and board[y][x] != 2:
                return True
    for x in range(len(board)):
        for y in range(len(board)-2):
            if board[y][x] == board[y+1][x] and board[y][x] == board[y+2][x] and board[y][x] != 2:
                return True
    for y in range(len(board)):
        for y1 in range(len(board)):
            if y1 !=y and board[y] == board[y1] and board[y].count(2) == 0:
                return True
    for x in range(len(board)): 
        column = []
        for y in range(len(board)):
            column.append(board[y][x])
        for x1 in range(len(board)): 
            column2 = []
            for y in range(len(board)):
                column2.append(board[y][x1])   
            if x != x1 and column == column2 and column.count(2) == 0:
                return True
    return False
def Solved(board):
    for y in range(len(board)):
        for x in range(len(board)):
            if board[y][x] == 2:
                return False
    if Mistake(board) == True:
        return False
    return True
def Rewind(save_board,save_data):
    i = len(save_board) - 1
    if save_data[i][2] == 1:
        save_board.pop()
        save_data.pop
        return Rewind(save_board,save_data)
    board = copy.deepcopy(save_board[i])
    save_data[i][2] = 1
    board[save_data[i][1]][save_data[i][0]] = 1
    return board,save_board,save_data

board = [[1,2,0,2,1,2],
[2,0,2,0,2,2],
[1,1,2,2,2,2],
[2,2,2,2,0,2],
[2,1,2,2,2,1],
[2,2,2,2,2,1]]
save_board = []
save_data = []
i=0
while Solved(board) == False and i < 20:
    if Mistake(board):
        print("EEEEEEEEEEEEEEE")
        board,save_board,save_data = Rewind(save_board,save_data)
    board_copy = copy.deepcopy(board)
    print(board,board_copy,"R")    
    board = AI(board)
    print(board,board_copy)
    if board == board_copy:
        print("WWWWWWWWWWWWWWWW")
        for line in AI(board):
            print(line)
        print("WWWWWWWWWWWWWWWW")
        done = False
        save_board.append(copy.deepcopy(board))
        for y in range(len(board)):
            for x in range(len(board)):
                if done == False and board[y][x] == 2:
                    board[y][x] = 0
                    save_data.append([x,y,0])
                    done = True
                    print(x,y)
    for line in AI(board):
        print(line)
    print("~~~~~~~~~~~~~~~~~~~~")
    i = i + 1

for line in AI(board):
    print(line)