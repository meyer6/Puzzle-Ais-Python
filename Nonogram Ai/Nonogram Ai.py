import copy
def Print_Board(board):
    for line in board:
        b=copy.deepcopy(line)
        for i in range(len(b)):
            if b[i]==1:
                b[i] = "x"
            if b[i]==0:
                b[i] = " "
            if b[i]==2:
                b[i] = "0"
            b[i]=str(b[i])
        print(b)
    print("_"*30)
def Solved(board):
    for line in board:
        if 0 in line:
            return False
    return True
def Valid(row,data):
    biggest = sorted(data)[::-1][0]
    row = ''.join(str(x) for x in row)
    if "2"*(biggest+1) in row:
        return False
    return True
def Ai(board,row_data,column_data):
    for y in range(len(row_data)):
        row = board[y]
        data = row_data[y]
        row3 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        for a in range(len(data)):
            row2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            num = data[a]

            x_before = 0
            full = True
            while x_before<len(row) and full:
                if row[x_before]!=1:
                    full=False
                else:
                    x_before = x_before + 1

            x_after = len(row)-1
            full = True
            while x_after>=0 and full:
                if row[x_after]!= 1:
                    full=False
                else:
                    x_after = x_after - 1

            total_before = sum(data[:a]) + a + x_before
            total_after = sum(data[a+1:]) + len(data) - a - 1 + (len(row)-x_after-1)

            possible_spaces = len(row) - total_before - total_after - num + 1
            possible_spaces2 = possible_spaces

            num_of_twos = 0
            start = 0
            full = True
            before = sum(data[:a])
            while start < len(row) and full == True:
                if row[start] == 0:
                    full=False
                elif before>0 and row[start]==2:
                    before = before - 1
                elif row[start]==2:
                    num_of_twos = num_of_twos + 1
                start = start +1
            end = len(row) - 1
            full = True
            after = sum(data[a+1:])
            while end >= 0 and full == True:
                if row[end] == 0:
                    full=False
                elif after>0 and row[end]==2:
                    after = after - 1
                elif row[end]==2:
                    num_of_twos = num_of_twos + 1
                end = end - 1
            
            if num_of_twos > num:
                num_of_twos = num
            if len(data) == 1:
                num_of_twos = row.count(2)
            if row.count(2)-(sum(data)-num)>num_of_twos:
                num_of_twos = row.count(2)-(sum(data)-num)

            for b in range(possible_spaces):
                row_backup = copy.deepcopy(row)
                row_backup[total_before + b : total_before + num  + b] = [2] * num
                if Valid(row_backup,data) and 1 not in row[total_before + b : total_before + num  + b] and row[total_before + b : total_before + num  + b].count(2)>=num_of_twos:
                    for x in range(total_before + b , total_before + num  + b):
                        row2[x] = row2[x] + 1
                        row3[x] = row3[x] + 1
                else:
                    possible_spaces2 = possible_spaces2 -1
            possible_spaces = possible_spaces2
            for x in range(len(row2)):
                if row2[x] == possible_spaces:
                    board[y][x] = 2
        for x in range(len(row3)):
            if row3[x] == 0:
                board[y][x] = 1

    for x in range(len(column_data)):
        column = []
        for y in range(len(column_data)):
            column.append(board[y][x])
        data = column_data[x]
        column3 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        for a in range(len(data)):
            column2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            num = data[a]

            x_before = 0
            full = True
            while x_before<len(column) and full:
                if column[x_before]!=1:
                    full=False
                else:
                    x_before = x_before + 1

            x_after = len(column)-1
            full = True
            while x_after>=0 and full:
                if column[x_after]!= 1:
                    full=False
                else:
                    x_after = x_after - 1

            total_before = sum(data[:a]) + a + x_before
            total_after = sum(data[a+1:]) + len(data) - a - 1 + (len(column)-x_after-1)

            possible_spaces = len(column) - total_before - total_after - num + 1
            possible_spaces2 = possible_spaces

            num_of_twos = 0
            start = 0
            full = True
            before = sum(data[:a])
            while start < len(column) and full == True:
                if column[start] == 0:
                    full=False
                elif before>0 and column[start]==2:
                    before = before - 1
                elif column[start]==2:
                    num_of_twos = num_of_twos + 1
                start = start +1
            end = len(column) - 1
            full = True
            after = sum(data[a+1:])
            while end >= 0 and full == True:
                if column[end] == 0:
                    full=False
                elif after>0 and column[end]==2:
                    after = after - 1
                elif column[end]==2:
                    num_of_twos = num_of_twos + 1
                end = end - 1
            if num_of_twos > num:
                num_of_twos = num
            if len(data) == 1:
                num_of_twos = column.count(2)
            if column.count(2)-(sum(data)-num)>num_of_twos:
                num_of_twos = column.count(2)-(sum(data)-num)
            #print(column,x,num,num_of_twos,possible_spaces)
            for b in range(possible_spaces):
                column_backup = copy.deepcopy(column)
                column_backup[total_before + b : total_before + num  + b] = [2] * num
                if Valid(column_backup,data) and 1 not in column[total_before + b : total_before + num  + b] and column[total_before + b : total_before + num  + b].count(2)>=num_of_twos:
                    for y in range(total_before + b , total_before + num  + b):
                        column2[y] = column2[y] + 1
                        column3[y] = column3[y] + 1
                else:
                    possible_spaces2 = possible_spaces2 - 1
            possible_spaces = possible_spaces2
            for y in range(len(column2)):
                if column2[y] == possible_spaces:
                    board[y][x] = 2
        for y in range(len(column3)):
            if column3[y] == 0:
                board[y][x] = 1

    return board    

board = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
row_data = [[1,8],[1,1,2,1],[15],[10],[1,2,1],[6,2,1],[1,10],[1,1,2,1],[6,2,1],[10],[1,2,1],[6,2,2],[1,10],[1,12],[15]]
column_data = [[1,1,1,1,1],[3,4,4],[1,1,1,1,1],[1,1,1,1,2],[1,1,1,1,2],[14],[1,2,1,1,3],[1,2,1,1,3],[1,2,1,1,3],[1,2,1,1,3],[15],[15],[1,2,1,1,3],[1,2,1,1,4],[14]]
i = 0
while Solved(board) == False and i<10:
    board_copy = copy.deepcopy(board)
    board = Ai(board,row_data,column_data)
    if board == board_copy:
        print("Same")
    Print_Board(board)
    i = i + 1