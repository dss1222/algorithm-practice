def solution(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                for k in range(i-1, i+2):
                    for l in range(j-1, j+2):
                        if k >= 0 and k < len(board) and l >= 0 and l < len(board[i]) and board[k][l] == 0:
                            board[k][l] = 2
    answer = 0
    for i in board:
        for j in i:
            if j == 0:
                answer += 1
    return answer
