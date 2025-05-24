#https://school.programmers.co.kr/learn/courses/30/lessons/120861
def solution(keyinput, board):
    x_range = board[0]//2
    y_range = board[1]//2
    x = 0
    y = 0
    for key in keyinput:
        if key == "left":
            x -= 1
        elif key == "right":
            x += 1
        elif key == "up":
            y += 1
        elif key == "down":
            y -= 1
            
        if x > x_range:
            x = x_range
        elif x < -x_range:
            x = -x_range
            
        if y > y_range:
            y = y_range
        elif y < -y_range:
            y = -y_range
            
    return [x, y]

def solution2(keyinput, board):
    curr = [0, 0]
    for k in keyinput:
        if k == 'left':
            curr[0] = max(curr[0] - 1, -(board[0] // 2))
        elif k == 'right':
            curr[0] = min(curr[0] + 1, board[0] // 2)
        elif k == 'down':
            curr[1] = max(curr[1] - 1, -(board[1] // 2))
        else:
            curr[1] = min(curr[1] + 1, board[1] // 2)

    return curr