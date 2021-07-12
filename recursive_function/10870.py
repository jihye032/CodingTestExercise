# 10870번 피보나치수 5
# https://www.acmicpc.net/problem/10870

def star(x, y):
    for n in range(x):
        for m in range(y):
            i = int(n/3)
            if i==1:
                if n%3==1 and m%3==1:
                    print(" ")
                else:
                    print("*")
            else :
                star(i, i)
        print("\n")


n = int(input())
star(n, n)