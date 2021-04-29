#!/usr/bin/python3
if __name__ == '__main__':
    a = 10
    b = 5
    from calculator_1 import addition
    print("{:d} + {:d} = {:d}".format(a, b, addition(a, b)))
    from calculator_1 import subtraction
    print("{:d} - {:d} = {:d}".format(a, b, subtraction(a, b)))
    from calculator_1 import multiplication
    print("{:d} * {:d} = {:d}".format(a, b, multiplication(a, b)))
    from calculator_1 import division
    print("{:d} / {:d} = {:.0f}".format(a, b, division(a, b)))