import copy
import itertools
def Print_Board(board):
    for line in board:
        print(line)
    print("_____________________")
def In_Range(x,y):
    if x>=0 and x<5 and y>=0 and y<5:
        return True
    return False
def In_Board(letter):
    for x in range(5):
        for y in range(5):
            if board[y][x]==letter:
                return [x,y]
    return [-1,-1]
def Existing_Possibilities(letter,p_board):
    pos=[]
    for x in range(5):
        for y in range(5):
            if letter in p_board[y][x]:
                pos.append([x,y])
    return pos
def Overlap(arr1,arr2):
    overlap=[]
    for line1 in arr1:
        for line2 in arr2:
            if line1==line2:
                overlap.append(line1)
    if arr1==[] or arr2==[]:
        overlap = arr1+arr2
    return overlap
def Remove_Duplicates(arr1):
    arr1.sort()
    return list(arr1 for arr1,_ in itertools.groupby(arr1))
def Set_p_board(board,words):
    p_board=[["","","","",""],["","","","",""],["","","","",""],["","","","",""],["","","","",""]]
    for word in words:
        for i in range(len(word)):
            if In_Board(word[i])[0]!=-1:
                possible_moves=[]
                for x1 in range(-1,2):
                    for y1 in range(-1,2):
                        x=In_Board(word[i])[0]+x1
                        y=In_Board(word[i])[1]+y1
                        if  not(x1==0 and y1==0) and In_Range(x,y) and board[y][x]=="":
                            possible_moves.append([x,y])
                for a in range(-1,2,2):
                    if i+a<len(word) and a==1 and In_Board(word[i+a])[0]==-1 or i+a>=0 and a==-1 and In_Board(word[i+a])[0]==-1:
                        existing_moves = Existing_Possibilities(word[i+a],p_board)
                        for coord in existing_moves:
                            p_board[coord[1]][coord[0]]=p_board[coord[1]][coord[0]].replace(word[i+a],"")
                        overlap = Overlap(possible_moves,existing_moves)
                        for coord in overlap:
                            p_board[coord[1]][coord[0]]=p_board[coord[1]][coord[0]]+word[i+a]
    p_board_b=copy.deepcopy(p_board)
    Print_Board(p_board)
    print("RRRRRRRRRRRRRRRRR")
    count=0
    while p_board_b!=p_board or count==0:
        p_board_b=copy.deepcopy(p_board)
        count=1
        for word in words:
            for i in range(len(word)):
                pos=Existing_Possibilities(word[i],p_board)
                possible_moves=[]
                for coord in pos:
                    for x1 in range(-1,2):
                        for y1 in range(-1,2):
                            x=coord[0]+x1
                            y=coord[1]+y1
                            if not(x1==0 and y1==0) and In_Range(x,y) and board[y][x]=="":
                                possible_moves.append([x,y])    
                for a in range(-1,2,2):
                    if (i+a<len(word) and a==1 or i+a>=0 and a==-1) and In_Board(word[i+a])[0]==-1:
                        print(word[i],pos,possible_moves,"E",word[i+a])
                        existing_moves = Existing_Possibilities(word[i+a],p_board)
                        if existing_moves==[]:
                            print(word[i+a])
                        for coord1 in existing_moves:
                            p_board[coord1[1]][coord1[0]]=p_board[coord1[1]][coord1[0]].replace(word[i+a],"")
                        overlap = Overlap(possible_moves,existing_moves)
                        overlap=Remove_Duplicates(overlap)
                        for coord1 in overlap:
                            p_board[coord1[1]][coord1[0]]=p_board[coord1[1]][coord1[0]]+word[i+a]  
        Print_Board(p_board_b)  
        Print_Board(p_board)
        print("TTTTTTTTTTTTTTTTTTTTTT")                          
    return p_board
def AI(board,words):
    p_board=Set_p_board(board,words)
    Print_Board(board)    
    Print_Board(p_board)
    print("wwwwwwwwwwwwwwwww")
    abc="abcdefghijklmnopqrstuvwxyz"
    for letter in abc:
        pos=Existing_Possibilities(letter,p_board)
        if In_Board(letter)[0]==-1 and len(pos)==1:
            board[pos[0][1]][pos[0][0]]=letter
    for x in range(5):
        for y in range(5):
            if len(p_board[y][x])==1:
                board[y][x]=p_board[y][x]
    return board

board = [["b","","r","","x"],["","","","",""],["v","","t","","q"],["","","","",""],["p","","d","","j"]]
words=["acquits","borax","fidget","inked","judicatory","muted","pets","solvent","swatch"]
for i in range(15):
    board=AI(board,words)
Print_Board(board)