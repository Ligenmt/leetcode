# 递归法
def fib1(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fib1(n-1) + fib1(n-2)


# 动态规划 备忘录法
def fib2(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    memo = []
    for i in range(n):
        memo.append(-1)
    memo.append(-1)

    def fib(nn, mm):
        if mm[nn] != -1:
            return mm[nn]
        if nn <= 2:
            return 1
        else:
            mm[nn] = fib(nn-1, mm) + fib(nn-2, mm)
        return mm[nn]
    return fib(n, memo)


print(fib2(50))

