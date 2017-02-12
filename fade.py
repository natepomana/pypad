#IMPORTS HERE




def run_fade(row_len, col_len):
    # create board
    board = [[0 for _ in range(row_len)] for _ in range(col_len)]
    board[0][0] = 1
    done = False
    while not done:
        # light launchpad up
        for i in range(row_len):
            for j in range(col_len):
                if board[i][j] == 0:
                    lp.LedCtrlXY(i, j + 1, 0, 0, 0)
                else:
                    lp.LedCtrlXY(i, j + 1, 100, 0, 0)
        # update board matrix
        for i in range(row_len - 1, -1, -1):
            for j in range(col_len - 1, -1, -1):
                if board[i][j] == 1:
                    if not i == row_len:
                        board[i+1][j] = 1
                    if not j == row_len - 1:
                        board[i][j+1] = 1
                    board[i][j] = 0
                    if i == row_len and j == col_len:
                        done = True


#run_fade(8,8)

