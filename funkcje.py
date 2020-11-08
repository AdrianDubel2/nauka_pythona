def calculator(a, b, op):
    if op == '+':
        return a + b
    if op == '*':
        return a * b
    if op == '/':
        return a / b
    if op == '-':
        return a - b
    return 0

if __name__ == '__main__':
    c = calculator(1, 2, '+')
    print(c)
    m = calculator(5, 4, '*')
    print(m)
    o = calculator(200, 100, '-')
    print(o)
    d = calculator(25, 5, '/')
    print(d)
