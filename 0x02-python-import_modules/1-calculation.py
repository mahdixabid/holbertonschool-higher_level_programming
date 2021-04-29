#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import addition, subtraction, multiplication, division
    a = 10
    b = 5
    print("{:d} + {:d} = {:d}".format(a, b, addition(a, b)))
    print("{:d} - {:d} = {:d}".format(a, b, subtraction(a, b)))
    print("{:d} * {:d} = {:d}".format(a, b, multiplication(a, b)))
    print("{:d} / {:d} = {:.0f}".format(a, b, division(a, b)))
