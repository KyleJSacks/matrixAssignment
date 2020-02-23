"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    l0 = ""
    l1 = ""
    l2 = ""
    l3 = ""
    for r in matrix:
        l0 += str(r[0]) + " "
        l1 += str(r[1]) + " "
        l2 += str(r[2]) + " "
        l3 += str(r[3]) + " "
    print(l0)
    print(l1)
    print(l2)
    print(l3)
#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident(matrix):
    for c in range(4):
        for r in range(4):
            matrix[c][r] = 0.0
    matrix[0][0] = 1.0
    matrix[1][1] = 1.0
    matrix[2][2] = 1.0
    matrix[3][3] = 1.0
    

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    placeholder = new_matrix(4, len(m2))
    for c in range(len(m2)):
        for v in range(4):
            row = []
            for i in range(4):
                row.append(m1[i][v])
                placeholder[c][v] = m_mult_row(row, m2[c])
    for c in placeholder:
        m2[placeholder.index(c)] = c

def m_mult_row(row, column):
    ans = 0
    for v in range(len(row)):
        ans += row[v] * column[v]
    return ans


def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0.0 )
    return m
