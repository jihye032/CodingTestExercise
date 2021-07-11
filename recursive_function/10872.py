# 10872번 팩토리얼
# https://www.acmicpc.net/problem/10872

def factorial(x):
    if x==1:
        return 1
    else :
        return x * factorial(x-1)

x = int(input())
print(factorial(x))
