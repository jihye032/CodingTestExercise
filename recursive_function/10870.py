# 10870번 피보나치수 5
# https://www.acmicpc.net/problem/10870

def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

n = int(input())
print(fibonacci(n))