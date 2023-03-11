def Letter_Indexes(letter,board):
    positions=[]
    for x in range(5):
        for y in range(5):
            if letter in board[y][x]:
                positions.append([x,y])
    return positions
def In_Range(x,y):
    if x>=0 and x<5 and y>=0 and y<5:
        return True
    return False
def In_Index(indexes,x,y):#not used rn

    if indexes==[]:
        return True
    for index in indexes:
        if index[0]==x and index[1]==y:
            return True
    return False
def Overlap(arr1,arr2):
    overlap=[]
    for line1 in arr1:
        for line2 in arr2:
            if line1==line2:
                overlap.append(line1)
    if arr1==[] or arr2==[]:
        overlap = arr1+arr2
    return overlap
def Remove_Letter(letter):
    for x in range(5):
        for y in range(5):
            p_board[y][x]=p_board[y][x].replace(letter,"")
def Possible(board,words,p_board):
    for word in words:
        for i in range(0,len(word)):
            index = Letter_Indexes(word[i],board)
            if index!=[]:
                if i<len(word)-1:
                    indexes_1 = Letter_Indexes(word[i+1],p_board)
                    possible_i1 = []
                    Remove_Letter(word[i+1])
                if i>0:
                    indexes_2 = Letter_Indexes(word[i-1],p_board)  
                    possible_i2 = []
                    Remove_Letter(word[i-1])
                for x1 in range(-1,2):
                    for y1 in range(-1,2):
                        x=index[0][0]+x1
                        y=index[0][1]+y1
                        if not(x1==0 and y1==0) and In_Range(x,y):
                            if i<len(word)-1:
                                possible_i1.append([x,y])
                            if i>0:
                                possible_i2.append([x,y])
                if i<len(word)-1:
                    overlap1=Overlap(indexes_1,possible_i1)
                    for line in overlap1:
                        p_board[line[1]][line[0]]=p_board[line[1]][line[0]]+word[i+1]
                if i>0:
                    overlap2=Overlap(indexes_2,possible_i2)
                    for line in overlap2:
                        p_board[line[1]][line[0]]=p_board[line[1]][line[0]]+word[i-1]
                
    return p_board
def Print_Board(board):
    for line in board:
        print(line)
    print("_____________________")


board = [["h","","","",""],["","","","",""],["","","l","",""],["","","","",""],["","","","","s"]]
p_board=[["","","","",""],["","","","",""],["","","","",""],["","","","",""],["","","","",""]]
words = ["helostr","hrclt"]
Print_Board(Possible(board,words,p_board))