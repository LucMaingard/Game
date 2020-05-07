#Tic Tack Toe

checkVert = []                           #variable to store column values
checkDiag = []                          #variable to store diagonal values


def game_board(player= " ", row=0, column=0):       #game function. 
    try:                                            
        if game[row][column] != " ":                #can't play on a space thats already been played
            print("This place is taken!")
        print( "      0    1    2")                 #column index
        game[row][column] = player
        
        for row in enumerate(game):                 #row index
            print(row)                          #print rows on new lines (form a grid)
        return game
    except:
        print ("Something went wrong!!!")           #in case user inputs index out of range



def win(game):                                  #function to check if game is won
    for row in game:                            #horizontal
        if row.count(row[0]) == len (row) and row[0] != " ":
            print("Winner, winner, chicken dinner!")
            game_won = True
            break

            
    for col in range(len(game)):                #vertical
        checkVert.append(row[col])              
        if checkVert.count(checkVert[0]) == len (checkVert) and checkVert[0] != " ":
            print("Winner, winner, chicken dinner!")
            game_won = True
            break


    for row in game:                           #diagonal
        if row[0] != " " or row[1] != " " or row[2] != " ":
            if game[0][0] == game [1][1] == game [2][2] or game[2][0] == game [1][1] == game [2][0]:
                print("Winner, winner, chicken dinner!")
                game_won = True
                break
            
play = True

while play:
    game = [[" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]]

    game_won = False
    game = game_board()
    
    while not game_won:                     #while game hasnt been won, it continues. below is user input
        row = int(input("which row would you like to play?"))
        column = int(input("which column would you like to play?"))
        player = input("are you playerX or playerO?")
        game_board(player, row, column)
        win(game)
        
          

        


