from turtle import Turtle


def In_Range(board,x,y):
    if x>=0 and x<len(board) and y>=0 and y<len(board):
        return True
    return False
def In_Array(arr,check):
    for line in arr:
        if line == check:
            return True
    return False
def Chain_Length(board,x,y):
    global length
    global past
    past.append([x,y])
    length = length + 1
    for x1 in range(-1,2,2):
        print(In_Array(past,[x+x1,y]),past,[x+x1,y])
        if In_Range(board,x+x1,y) and board[y][x+x1]==board[y][x] and In_Array(past,[x+x1,y])==False:
            Chain_Length(board,x+x1,y)
    for y1 in range(-1,2,2):
        if In_Range(board,x,y+y1) and board[y+y1][x]==board[y][x] and In_Array(past,[x,y+y1])==False:
            Chain_Length(board,x,y+y1)
def Ai(board):
    global length
    global past
    for x in range(len(board)):
        for y in range(len(board)):
            if board[y][x] != "" and str(board[y][x])[0]!="b":
                length = 0
                past = []
                Chain_Length(board,x,y)
                if length == board[y][x]:
                    for coord in past:
                        for x1 in range(-1,2,2):
                            if In_Range(coord[0]+x1,coord[1]):
                                board[coord[1]][coord[0]+x1] = "b"
                        for y1 in range(-1,2,2):
                            if In_Range(coord[0]+x1,coord[1]):
                                board[coord[1]][coord[0]+x1] = "b"
    return board
board = [["4","4","4","","","",""],
["","","4","","","",""],
["","","","","","",""],
["","","","","","",""],
["","","","","","",""],
["","","","","","",""],
["","","","","","",""]]
length = 0
past = []
print(Ai(board))