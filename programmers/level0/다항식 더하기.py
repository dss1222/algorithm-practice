def solution(polynomial):
    polynomial = polynomial.split(" + ")
    x_num = 0
    num = 0
    for i in polynomial:
        if "x" in i:
            if i == "x":
                x_num += 1
            else:
                x_num += int(i.replace("x", ""))
        else:
            num += int(i)
    if x_num == 0:
        return str(num)
    
    if x_num == 1:
        x_num = "x"
    elif x_num > 1:
        x_num = str(x_num) + "x"

    if num == 0:
        return x_num
    else:
        return x_num + " + " + str(num)
