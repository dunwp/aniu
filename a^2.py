# 计算a*a + b*b + c*c
def calc(*numbers):
    sum= 0
    for n in numbers:
        sum= sum+n*n
    return sum
