board=[ 
      [  [1, None,4],
      [3, None,None],
      [None, 7,6]  ], 
    
      [  [None, None,2],
      [None, None,5],
      [None, 4,8]  ],  
      
      [  [5, None,None],
      [None, None,7],
      [None, None,None]  ],    
      
      [  [None, 3,8],
      [2, 9,None],
      [7, None,1]  ],
      
      [  [None, None,None],
      [None, None,None],
      [None, None,None]  ],
      
      [  [7, None,2],
      [None, 1,4],
      [3, 8,None]  ],
      
      [  [None, None,None],
      [9, None,None],
      [None, None,2]  ],
      
      [  [6, 2,None],
      [4, None,None],
      [7, None,None]  ],
      
      [  [4, 5,None],
      [None, None,8],
      [1, None,3]  ],
      
                        ]

'''square is 1 unit;
    box has 9 squares, with 3 by 3 dimensions
        board has 9 boxes and 81 square, dimension is 3 by 3 boxes'''
                        
def get_cell(value):
    ''' if value of the cell is equal to None, converts it to an empty space on the board'''
    if value is None:
        return " "
    return value

def draw_pretty_board(board):
    '''Draws out a board based on the above lists within lists within lists. Board contains 9 boxes with 3 by 3 dimensions and 81 squares 9 by 9 in dimension'''
    print "    C1   C2  C3  C4  C5  C6   C7  C8   C9"
    print "   _______________________________________"
    print "R{0} |_{1}_|_{2}_|_{3}_||_{4}_|_{5}_|_{6}_||_{7}_|_{8}_|_{9}_|".format(1,get_cell(board[0][0][0]),get_cell(board[0][0][1]),get_cell(board[0][0][2]), get_cell(board[1][0][0]),get_cell(board[1][0][1]),get_cell(board[1][0][2]), get_cell(board[2][0][0]),get_cell(board[2][0][1]),get_cell(board[2][0][2]))
    print "R{0} |_{1}_|_{2}_|_{3}_||_{4}_|_{5}_|_{6}_||_{7}_|_{8}_|_{9}_|".format(2,get_cell(board[0][1][0]),get_cell(board[0][1][1]),get_cell(board[0][1][2]), get_cell(board[1][1][0]),get_cell(board[1][1][1]),get_cell(board[1][1][2]), get_cell(board[2][1][0]),get_cell(board[2][1][1]),get_cell(board[2][1][2]))
    print "R{0} |_{1}_|_{2}_|_{3}_||_{4}_|_{5}_|_{6}_||_{7}_|_{8}_|_{9}_|".format(3,get_cell(board[0][2][0]),get_cell(board[0][2][1]),get_cell(board[0][2][2]), get_cell(board[1][2][0]),get_cell(board[1][2][1]),get_cell(board[1][2][2]), get_cell(board[2][2][0]),get_cell(board[2][2][1]),get_cell(board[2][2][2]))
    print "   ----------------------------------------"
    print "R{0} |_{1}_|_{2}_|_{3}_||_{4}_|_{5}_|_{6}_||_{7}_|_{8}_|_{9}_|".format(4,get_cell(board[3][0][0]),get_cell(board[3][0][1]),get_cell(board[3][0][2]), get_cell(board[4][0][0]),get_cell(board[4][0][1]),get_cell(board[4][0][2]), get_cell(board[5][0][0]),get_cell(board[5][0][1]),get_cell(board[5][0][2]))
    print "R{0} |_{1}_|_{2}_|_{3}_||_{4}_|_{5}_|_{6}_||_{7}_|_{8}_|_{9}_|".format(5,get_cell(board[3][1][0]),get_cell(board[3][1][1]),get_cell(board[3][1][2]), get_cell(board[4][1][0]),get_cell(board[4][1][1]),get_cell(board[4][1][2]), get_cell(board[5][1][0]),get_cell(board[5][1][1]),get_cell(board[5][1][2]))
    print "R{0} |_{1}_|_{2}_|_{3}_||_{4}_|_{5}_|_{6}_||_{7}_|_{8}_|_{9}_|".format(6,get_cell(board[3][2][0]),get_cell(board[3][2][1]),get_cell(board[3][2][2]), get_cell(board[4][2][0]),get_cell(board[4][2][1]),get_cell(board[4][2][2]), get_cell(board[5][2][0]),get_cell(board[5][2][1]),get_cell(board[5][2][2]))
    print "   ----------------------------------------"
    print "R{0} |_{1}_|_{2}_|_{3}_||_{4}_|_{5}_|_{6}_||_{7}_|_{8}_|_{9}_|".format(7,get_cell(board[6][0][0]),get_cell(board[6][0][1]),get_cell(board[6][0][2]), get_cell(board[7][0][0]),get_cell(board[7][0][1]),get_cell(board[7][0][2]), get_cell(board[8][0][0]),get_cell(board[8][0][1]),get_cell(board[8][0][2]))
    print "R{0} |_{1}_|_{2}_|_{3}_||_{4}_|_{5}_|_{6}_||_{7}_|_{8}_|_{9}_|".format(8,get_cell(board[6][1][0]),get_cell(board[6][1][1]),get_cell(board[6][1][2]), get_cell(board[7][1][0]),get_cell(board[7][1][1]),get_cell(board[7][1][2]), get_cell(board[8][1][0]),get_cell(board[8][1][1]),get_cell(board[8][1][2]))
    print "R{0} |_{1}_|_{2}_|_{3}_||_{4}_|_{5}_|_{6}_||_{7}_|_{8}_|_{9}_|".format(9,get_cell(board[6][2][0]),get_cell(board[6][2][1]),get_cell(board[6][2][2]), get_cell(board[7][2][0]),get_cell(board[7][2][1]),get_cell(board[7][2][2]), get_cell(board[8][2][0]),get_cell(board[8][2][1]),get_cell(board[8][2][2]))
    return

def enter_num():
    '''Asks user for number selection to place on board. Checks to make sure number is from 1 to 9'''
    invalid_input = True 
    while invalid_input: 
        user_num_choice = raw_input("Please choose a number from 1-9: ")
        if int(user_num_choice) < 10 and int(user_num_choice) > 0:
            invalid_input = False
        elif type(user_num_choice) != 'int':
            print "Invalid Entry! Please enter an integer"
        else:
            print "Number is greater than 9 or less than 1"
    return user_num_choice

def enter_row_location():
    '''asks user for row location of the square on the board and returns that number. Checks to make sure number is from 1 to 9 '''
    invalid_input = True 
    while invalid_input: 
        row_selection = int(raw_input("Please choose a row from 1-9: "))
        if row_selection < 10 and row_selection > 0:
            invalid_input = False
        else: 
            print "Row is greater than 9 or less than 1"
    return row_selection


def enter_column_location():
    '''asks user for column location of the square on the board and returns that number. Checks to make sure number is from 1 to 9 '''
    invalid_input = True 
    while invalid_input:
        column_selection = int(raw_input("Please choose a column from 1-9: "))
        if column_selection < 10 and column_selection > 0:
            invalid_input = False
        else: 
            print "Column is greater than 9 or less than 1"
    return column_selection
    

def find_box_row_index(board_row_location):
    '''finds the index of the row of each box within the board '''
    return (board_row_location -1)% 3

def find_box_col_index(board_col_location):
    '''find the index fo the column of each box within the board '''
    return (board_col_location-1) % 3 

    
def find_possible_boxes_by_row(row_location):
    '''based on the row number that was entered by the user, this function returns a list of the indices of possible 3 boxes that row may span. 
       Will need this to help determine the index of the square the user selected''' 
    if row_location > 0 and row_location < 4: 
        return [0,1,2]
    elif row_location > 3 and row_location < 7: 
        return [3,4,5]
    elif row_location > 6 and row_location < 10: 
        return [6,7,8]
    
def find_possible_boxes_by_column(column_location):
    '''based on the column number that was entered by the user, this function returns a list of the indices of the 3 boxes that column will span. Will need this to help determine the index of the square the user selected''' 
    if column_location > 0 and column_location < 4: 
        return [0,3,6]
    elif column_location > 3 and column_location < 7: 
        return [1,4,7]
    elif column_location > 6 and column_location < 10: 
        return [2,5,8]   

def intersect(a, b):
    ''' return the intersection of two lists '''
    return list(set(a) & set(b))[0]
    

def find_box_index(board_column_location, board_row_location):
    '''this number identifies the index of the box of where to place the number based on two earlier functions and returns this boxes index'''
    list_of_column_boxes = find_possible_boxes_by_column(board_column_location)
    list_of_row_boxes = find_possible_boxes_by_row(board_row_location)
    box_index= intersect(list_of_row_boxes,list_of_column_boxes)
    return box_index
    
    
def check_a_row_in_board(board, user_num_choice, row_index): 
    ''' checks to make sure that there are no identical numbers in each column of the large board and return the boolean, true or false. Need to check multiple boxes'''
    box_subsection = []
    box_subsection_list = []
    if row_index > 0  and row_index < 4: 
         box_subsection = [0,1,2]
    elif row_index > 3 and row_index < 7: 
         box_subsection = [3,4,5]
    elif row_index > 6 and row_index < 10: 
         box_subsection = [6,7,8]
    
    for num in box_subsection: 
        box_subsection_list.append(board[num])
 
    for box in box_subsection_list:
        if user_num_choice in box[(row_index-1) % 3]:
            return False 
    
    return True 

def check_a_column_in_board(board, user_num_choice, column_index):
    '''checks to make sure there are no identical numbers in each colum on the large board. It does this by finding the 3 boxes this column passes and the index in these boxes. Need to check multiple boxes''' 
    box_subsection = []
    box_subsectoin_list = []
    if column_index > 0  and column_index < 4: 
        box_subsection = [0,3,6]
    elif column_index > 3 and column_index < 7: 
        box_subsection = [1,4,7]
    elif column_index > 6 and column_index < 10: 
        box_subsection = [2,5,8] 
    
    for num in box_subsection:
        box_subsectoin_list.append(board[num])
    
    for box in box_subsectoin_list:
        for row in box:
            if row[(column_index-1) % 3] ==  user_num_choice:
                return False 
    
    return True 
        


def check_a_box_in_board(board, user_num_choice, box_index):
    '''checks to make sure that there are no identical numbers in a single 3 by 3 box by taking in the board and checking the box'''
    list_of_row_numbers = []
    for row in board[box_index]:
        for square in row:
            list_of_row_numbers.append(square)
    if user_num_choice in list_of_row_numbers:
        return False
    else:
        return True  
        
        
def check_board(board): 
    '''checks to make sure the entire booard does not have any repeat numbers that contradict the game rules; 
            returns boolean and updated box if number meets conditions'''
    # enter some nice print statements 
    user_num_choice = enter_num()
    board_row_location = enter_row_location()
    board_column_location = enter_column_location()
    box_index = find_box_index(board_column_location,board_row_location)
    box_column_index = find_box_col_index(board_column_location)
    box_row_index = find_box_row_index(board_row_location)
    print "You entered {0} at row {1} and column {2}".format(user_num_choice,board_row_location, board_column_location)
    checking_a_row_in_a_board = check_a_row_in_board(board, user_num_choice, board_row_location)
    checking_a_column_in_a_board = check_a_column_in_board(board, user_num_choice, board_column_location)
    checking_box = check_a_box_in_board(board,user_num_choice, box_index)
    if checking_box == True and checking_a_column_in_a_board == True and checking_a_row_in_a_board == True: 
        board[box_index][box_row_index][box_column_index] = user_num_choice
        print "Adding {0} to box {1} at row {2} and column {3}".format(user_num_choice,box_index, box_row_index, box_column_index)
        return True,board
    else: 
        return False,board 


def check_if_board_is_full(board):
    ''' checks to see if the board only has numbers and no more None and breaks program'''
    for box in board:
        for row in box:
            if None in row:
                return False
    return True 


    
def run_game(board):
    ''' Greetshe User, Provides Instructions, and run function and break when the board is full of numbers'''
    print "Welcome to Game of Sudoku!"
    while not check_if_board_is_full(board):
        draw_pretty_board(board)
        checking_board, board = check_board(board)
        if checking_board == True:
            print "Updated Board"
        else:
            print "Number already Exists in box, column, or row! Enter a new Number\n"
            
    print "Great Job! Now Ending Game!"
    


run_game(board)
