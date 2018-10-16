def size_of_board():
    while True:
        the_size = int(input("Input dimension of the board: "))
        if the_size >= 3:
            break
    return the_size

def get_list_board(the_size):
    i = 1
    j = 0
    big_list = []
    while i <= the_size:
        one_list = []
        for k in range((j*the_size),(i*the_size)):
            one_list.append((k+1))
        big_list.append(one_list)
        i +=1
        j +=1
    return big_list

def print_board(list_of_lists):
    for row in list_of_lists:
        for colum in row:
            print('{:>5}'.format(colum), end=' ')
        print()

def move(list_of_lists, the_size, i):
    while True:
        row_nr = 0
        counter = 0
        if i%2 == 0:
            index = int(input('X position: '))
        else: 
            index = int(input('O position: '))
        for row in list_of_lists:
            try:
                row = row
                place = row.index(index)
                row.remove(place+1+(row_nr*the_size))
                if i%2 == 0:
                    row.insert(place, 'X')
                else: 
                    row.insert(place, 'O')
                counter += 1
            except:
                None
            row_nr +=1
        if counter == 1:
            break
        else:
            print("Illegal move!")

def winner(the_current_board, the_size):
    k = 0
    while (k+1)<the_size:
        down = 0
        diagonal1 = 0
        diagonal2 = 0
        sides = 0
        for b in range(0,the_size-1): 
            if the_current_board[b][k] != the_current_board[b+1][k]:
                break
            else:
                down +=1
        for b in range(0,the_size-1): 
            if the_current_board[k][b] != the_current_board[k][b+1]:
                break
            else:
                sides +=1
        if down == (the_size-1) or sides == (the_size -1):
            return 1
        k +=1
    for b in range(0, the_size-1):
        if the_current_board[b][b] != the_current_board[b+1][b+1]:
            break
        else:
            diagonal1 +=1
    for b in range(0, the_size-1):
        if the_current_board[the_size-b-1][b] != the_current_board[the_size-b-2][b+1]:
            break
        else:
            diagonal2 +=1
    if diagonal1 == (the_size - 1) or diagonal2 ==(the_size -1):
        return 1

    return 0

the_size = size_of_board()
the_current_board = get_list_board(the_size)
print_board(the_current_board)
for i in range(the_size**2):
    move(the_current_board ,the_size, i)
    dub = winner(the_current_board, the_size)
    print_board(the_current_board)
    if dub == 1:
        if i%2 == 0:
            print("Winner is: X")
        else:
            print("Winner is: O")
        break
    if i == (the_size **2)-1:
        print("Draw!")
        break