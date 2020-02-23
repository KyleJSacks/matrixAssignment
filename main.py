from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()
matrix[0][0] = 2.0
matrix[1][1] = 3.0
matrix[2][2] = 4.0
matrix[3][3] = 5.0
matrix2 = new_matrix(4, 2)
for c in range(2):
    for r in range(4):
        matrix2[c][r] = float(c + r)
print("m1:")
print_matrix(matrix)
#print('\n')
#ident(matrix)
#print_matrix(matrix)
print('\n')
print("m2:")
print_matrix(matrix2)
print('\n')
matrix_mult(matrix, matrix2)
print("m1 * m2:")
print_matrix(matrix2)

matrix = new_matrix(0, 0)


add_point(matrix, 255, 255)
add_point(matrix, 100, 300)
add_edge(matrix, 0, 0, 0, 400, 200, 0)
 
draw_lines( matrix, screen, color )
display(screen)
