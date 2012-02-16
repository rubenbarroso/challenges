# coding=utf-8
"""
From http://programmingpraxis.com/2011/12/06/pascals-triangle/

In 1653 Blaise Pascal published his treatise Traité du triangle arithmétique
describing his triangle computing the binomial coefficients, which are used
in the study of probability; Pascal gets credit for the name even though
both the coefficients and their arrangement in a triangle were known before
him.

To compute the triangle, start with a row containing only 1. Then each
succeeding row is built by adding the two numbers triangularly above the
current number, assuming a temporary 0 at each end of the prior row.

Your task is to write a program to neatly display Pascal’s Triangle.
"""

def c(n, k):
    """ A Pascal's Triangle simply represents the binomial coefficients """
    if k == 0 or k == n:
        return 1
    else:
        return c(n - 1, k - 1) + c(n - 1, k)

#Tests
assert c(0, 0) == 1
assert c(1, 0) == 1
assert c(1, 1) == 1
assert c(2, 0) == 1
assert c(2, 1) == 2
assert c(2, 2) == 1
assert c(3, 0) == 1
assert c(3, 1) == 3
assert c(3, 2) == 3
assert c(3, 3) == 1


def pascal(n=6):
    """ Pretty-print a Pascal's Triangle until a specific row n (0-indexed) """

    def indent_fill(line, line_size):
        return ' ' * ((line_size - len(line)) / 2)

    lines = []
    line_size = 0
    for i in range(n):
        coefficients = []
        for j in range(i + 1):
            coefficients.append(str(c(i, j)))
        line = ' '.join(coefficients)
        line_size = max(len(line), line_size)
        lines.append(line)

    for line in lines:
        print indent_fill(line, line_size) + line + indent_fill(line, line_size)

#Test
pascal()

#Output
#
#      1
#     1 1
#    1 2 1
#   1 3 3 1
#  1 4 6 4 1
# 1 5 10 10 5 1