import copy
def subset_sum(numbers, target, partial=[]):
    global possible_nums
    s = sum(partial)

    # check if the partial sum is equals to target
    if s == target: 
        possible_nums.append(partial)
    if s >= target:
        return  # if we reach the number why bother to continue
    
    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        subset_sum(remaining, target, partial + [n])
def Overlap(str1,str2):
    overlap = ""
    for letter in str1:
        if letter in str2:
            overlap = overlap + letter
    return overlap
def Set_P_Board(h_board,v_board):
    global possible_nums
    p_board = []
    for i in range(len(h_board)):
            p_board.append(["x"]*len(h_board[0]))
    for y in range(len(h_board)):
        for x in range(len(h_board[0])):
            if h_board[y][x]=="x":
                existing_nums=[]
                x1 = 1
                while x + x1 < len(h_board[0]) and h_board[y][x + x1][0] != "*"and h_board[y][x + x1][0] != ".":
                    if h_board[y][x + x1] != "x":
                        existing_nums.append(int(h_board[y][x + x1]))
                    x1 = x1 + 1

                x2 = -1
                while x + x2 >= 0 and h_board[y][x + x2][0] != "*":
                    if h_board[y][x + x2] != "x":
                        existing_nums.append(int(h_board[y][x + x2]))
                    x2 = x2 - 1
                if x + x2 > -1:
                    target_num = int(h_board[y][x + x2][1:])
                    nums2 = [1,2,3,4,5,6,7,8,9]
                    for num in existing_nums:
                        nums2.remove(num)
                        target_num = target_num - num

                    length = x1 - x2 - 1 - len(existing_nums)
                    
                    possible_nums=[]
                    subset_sum(nums2,target_num)
                    for i in range(len(possible_nums)-1,-1,-1):
                        set = possible_nums[i]
                        if len(set) != length:
                            possible_nums.pop(i)
                    possible_nums = [x for xs in possible_nums for x in xs]
                    possible_nums = list(dict.fromkeys(possible_nums))
                    possible_nums = ''.join(str(x) for x in possible_nums)

                    if p_board[y][x]=="x":
                        p_board[y][x] = possible_nums
                    else:
                        p_board[y][x] = Overlap(p_board[y][x],possible_nums)
            if v_board[y][x]=="x":
                existing_nums=[]
                y1 = 1
                while y + y1 < len(v_board) and v_board[y + y1][x][0] != "*" and v_board[y + y1][x][0] != ".":
                    if v_board[y + y1][x] != "x":
                        existing_nums.append(int(v_board[y + y1][x]))
                    y1 = y1 + 1

                y2 = -1
                while y + y2 >= 0 and v_board[y + y2][x][0] != "*":
                    if v_board[y + y2][x] != "x":
                        existing_nums.append(int(v_board[y + y2][x]))
                    y2 = y2 - 1
                if y + y2 > -1:
                    target_num = int(v_board[y + y2][x][1:])
                    nums2 = [1,2,3,4,5,6,7,8,9]
                    for num in existing_nums:
                        nums2.remove(num)
                        target_num = target_num - num

                    length = y1 - y2 - 1 - len(existing_nums)
                    
                    possible_nums=[]
                    subset_sum(nums2,target_num)
                    for i in range(len(possible_nums)-1,-1,-1):
                        set = possible_nums[i]
                        if len(set) != length:
                            possible_nums.pop(i)
                    possible_nums = [x for xs in possible_nums for x in xs]
                    possible_nums = list(dict.fromkeys(possible_nums))
                    possible_nums = ''.join(str(x) for x in possible_nums)
                    if p_board[y][x]=="x":
                        p_board[y][x] = possible_nums
                    else:
                        p_board[y][x] = Overlap(p_board[y][x],possible_nums)
    return p_board
def Ai(h_board,v_board):
    p_board = Set_P_Board(h_board,v_board)
    for y in range(len(p_board)):
        for x in range(len(p_board[0])):
            if p_board[y][x]!="x" and len(p_board[y][x]) == 1:
                h_board[y][x] = p_board[y][x]
                v_board[y][x] = p_board[y][x]
    return h_board,v_board
def Solved(h_board):
    for line in h_board:
        if "x" in line:
            return False
    return True
def Mistake(p_board):
    for line in p_board:
        if "" in line:
            return True
    return False   
def Rewind(save_h_board,save_v_board,save_data):
    index = len(save_h_board)-1
    print(index,save_h_board,save_data)
    h_board = copy.deepcopy(save_h_board[index])
    v_board = copy.deepcopy(save_v_board[index])
    save_data[index][3] = save_data[index][3] + 1
    if save_data[index][3] == len(save_data[index][2]) :
        save_h_board.pop()
        save_v_board.pop()
        save_data.pop()
        return Rewind(save_h_board,save_v_board,save_data)
    h_board[save_data[index][1]][save_data[index][0]] = save_data[index][2][save_data[index][3]]
    v_board[save_data[index][1]][save_data[index][0]] = save_data[index][2][save_data[index][3]]
    return h_board,v_board,save_h_board,save_v_board,save_data

possible_nums=[]
h_board=[[".",".",".",".",".",".",".","."],
[".","*5","x","x",".",".",".","."],
["*17","x","x","x","x",".",".","."],
["*16","x","x","*12","x","x",".","."],
["*10","x","x",".","*17","x","x","."],
[".","*13","x","x",".","*17","x","x"],
[".",".","*6","x","x","*7","x","x"],
[".",".",".","*24","x","x","x","x"],
[".",".",".",".","*7","x","x","."]]

v_board=[[".",".","*25","*4",".",".",".","."],
[".","*22","x","x","*13",".",".","."],
[".","x","x","x","x","*14",".","."],
[".","x","x",".","x","x","*32","."],
[".","x","x","*9",".","x","x","*22"],
[".",".","x","x","*3",".","x","x"],
[".",".",".","x","x","*7","x","x"],
[".",".",".",".","x","x","x","x"],
[".",".",".",".",".","x","x","."]]
save_h_board = []
save_v_board = []
save_data =[]
for line in Set_P_Board(h_board,v_board):
    print(line)
i=0
while i<100 and Solved(h_board)==False:
    p_board = Set_P_Board(h_board,v_board)
    if Mistake(p_board):
        print(p_board)
        h_board,v_board,save_h_board,save_v_board,save_data = Rewind(save_h_board,save_v_board,save_data)
    save_board = copy.deepcopy(h_board)
    h_board,v_board = Ai(h_board,v_board)

    p_board = Set_P_Board(h_board,v_board)
    if Mistake(p_board)==False and h_board == save_board:
        print(h_board,p_board,"EEEEEEEEE")
        done = False
        for y in range(len(p_board)):
            for x in range(len(p_board[0])):
                if p_board[y][x]!="x" and done == False:
                    done=True
                    save_h_board.append(copy.deepcopy(h_board))
                    save_v_board.append(copy.deepcopy(v_board))
                    h_board[y][x] = p_board[y][x][0]
                    v_board[y][x] = p_board[y][x][0]
                    save_data.append([x,y,p_board[y][x],0])
    for line in h_board:
        print(line)
    print("WWWWWWWWWWW")


    i = i + 1
print(h_board,v_board)
print(Set_P_Board(h_board,v_board))
for line in h_board:
    print (line)