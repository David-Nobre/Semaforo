from board import Board

def get_row_col (initiate_board : bool = False) -> int:

    try :
        row = str (input ('linha? '))
        col = int (input ('coluna? '))
    except:
        print ('Erro na introduçao de dados')

    if initiate_board:
        try:
            row = int (row)
        except:
            print ('row must be an integer')
    else:
        row = ord (row) - ord ('A')
        col -= 1
    return row, col

def interaction(board : Board) -> None:
    while (True):

        row, col = get_row_col ()

        if board.in_bounds (row, col):
            board.make_play(row, col)
            board.draw_board()
        
        if board.check_winner():
            print ('Winner!')    
            cmd = input ('continue? ')
            if cmd == 'n':
                break
            main()

def main ():
    rows, cols = get_row_col (initiate_board = True)
    board = Board(rows, cols)
    board.draw_board()
    interaction(board)

if __name__ == '__main__':
    main ()