def abs(x):
    ''' Returns the Absolute value of x'''
    if x > 0:
        return x
    return -x

def sign(x):
    ''' Returns the sign of x in 1/-1'''
    if x > 0:
        return 1
    return -1

def vector_normalize(vector):
    '''Returns unitary vector'''
    c = (vector[0]**2 + vector[1]**2)**(1/2)
    if c > 0:
        return (vector[0]/c, vector[1]/c)

def direction_vector(A, B):
    '''Return direction vector normalized AB'''
    return vector_normalize((B[0]-A[0], B[1]-A[1]))

def distance(A, B):
    '''Returns the Distance^2'''
    return (((B[0] - A[0] )**2) + ((B[1]-A[0])**2)) # Distance Formula

def line_intersection(line1, line2):
    '''Returns the point of Intersection between Line 1 and Line 2'''

    def determinant(a, b):
        return a[0] * b[1] - a[1] * b[0]

    x_diff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    y_diff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])


    div = determinant(x_diff, y_diff)
    if div == 0:
       return

    d = (determinant(line1[0], line1[1]), determinant(line2[0], line2[1]))
    x = determinant(d, x_diff) / div
    y = determinant(d, y_diff) / div

    x = round(x)
    y = round(y)
    x_min_line1 = round(min(line1[0][0], line1[1][0]))
    x_min_line2 = round(min(line2[0][0], line2[1][0]))
    x_max_line1 = round(max(line1[0][0], line1[1][0]))
    x_max_line2 = round(max(line2[0][0], line2[1][0]))
    y_min_line1 = round(min(line1[0][1], line1[1][1]))
    y_min_line2 = round(min(line2[0][1], line2[1][1]))
    y_max_line1 = round(max(line1[0][1], line1[1][1]))
    y_max_line2 = round(max(line2[0][1], line2[1][1]))

    if x < x_min_line1 or x > x_max_line1 or x < x_min_line2 or x > x_max_line2:
        return
    if y < y_min_line1 or y > y_max_line1 or y < y_min_line2 or y > y_max_line2:
        return

    return [x, y]
