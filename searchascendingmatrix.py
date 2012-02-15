# coding=utf-8
"""
From http://programmingpraxis.com/2012/02/10/search-in-an-ascending-matrix/

Search In An Ascending Matrix
February 10, 2012

Today’s exercise is taken from our inexhaustible list of interview questions:

Given an m by n matrix of integers with each row and column in ascending order,
search the matrix and find the row and column where a key k appears, or report
that k is not in the matrix. For instance, in the matrix

 1  5  7  9
 4  6 10 15
 8 11 12 19
14 16 18 21

the key 11 appears in row 2, column 1 (indexing from 0) and the key 13 is not
present in the matrix. The obvious algorithm takes time O(m x n) to search the
matrix row-by-row, but you must exploit the order in the matrix to find an
algorithm that takes time O(m + n).

Your task is to write the requested search function.
"""

def search(k, matrix):
    """ We loop over the diagonal elements looking for the first one greather
        than the number.Then, we carry out a linear search over the elements
        from the previous diagonal element -what we refer to as pivot- and
        the current one. It is easily seen that this algorithm is O(m + n). """

    def linear_search(k, list):
        for i in range(len(list)):
            pivot = list[i]
            if k == pivot:
                return i
        return -1

    m = len(matrix)
    for i in range(m):
        pivot = matrix[i][i]
        if k == pivot:
            return i, i
        elif k < pivot:
            if i is 0:
                # upper left element bigger than searched number,
                # hence all elements of the matrix bigger also
                # therefore not present
                return -1
            else:
                lower_slice = matrix[i - 1][i:]
                lower_index = linear_search(k, lower_slice)
                if lower_index != -1:
                    return i - 1, i + lower_index

                upper_slice = matrix[i][0:i]
                upper_index = linear_search(k, upper_slice)
                if upper_index != -1:
                    return i, upper_index
                    # not found
    return -1

# Tests
matrix = [[1, 5, 7, 9],
    [4, 6, 10, 15],
    [8, 11, 12, 19],
    [14, 16, 18, 21]]

assert search(11, matrix) == (2, 1)
assert search(5, matrix) == (0, 1)
assert search(1, matrix) == (0, 0)
assert search(22, matrix) == -1
assert search(13, matrix) == -1
assert search(14, matrix) == (3, 0)
assert search(21, matrix) == (3, 3)

