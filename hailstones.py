# coding=utf-8
"""
From http://programmingpraxis.com/2012/02/17/hailstones

Consider the sequence of positive integers for which xn+1 = xn / 2 when x is even and 3·xn + 1 when
xn is odd; this is known colloquially as “half or triple plus one.” For instance, starting from
x0 = 13 the sequence is 13, 40, 20, 10, 5, 16, 8, 4, 2, 1, whence it loops through 4, 2, 1, ….
This is called a hailstone sequence because it tends to go up and down and up and down much like
hailstones in a thundercloud. Lothar Collatz conjectured in 1937 that every starting number
eventually reaches 1; the conjecture is widely believed to be true, but has never been proven
or disproven.

Your task is to write a function that computes hailstone sequences; you may wish to have some fun
with your function by searching the internet for interesting tidbits about hailstone sequences and
the Collatz conjecture.
"""

def hailstone(x):
    """ A wondrous number is one which eventually reaches 1 using this function.
        See GEB pages 400 and 401. """
    seq = [x]
    while x != 1:
        # how I miss tail-call optimization in Python
        if not x % 2:
            x /= 2
        else:
            x = 3 * x + 1
        seq.append(x)
    return seq

# Test
print hailstone(15)

# Output
# [15, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1]
