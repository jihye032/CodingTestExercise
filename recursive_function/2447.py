def stars(star):
    matrix = []
    for i in range( len(star) * 3 ):
        if i // len(star) == 1:
            matrix.append(star[i%len(star)] + " " * len(star) + star[i%len(star)])
        else :
            matrix.append(star[i%len(star)] * 3)
    return(list(matrix))


if __name__ == "__main__":
    x = int(input())

    num = 0
    while x > 3:
        x = int(x/3)
        num += 1
    
    star = ["***", "* *", "***"]
    for i in range(num):
        star = stars(star)
    
    for i in star:
        print(i)