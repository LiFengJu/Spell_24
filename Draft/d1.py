# 打印斐波那契数列的前十项

def print_fibonacci(n):
    a,b = 0,1
    for _ in range(n):
        print(a, end=' ')
        a,b = b,a+b

print_fibonacci(10)

