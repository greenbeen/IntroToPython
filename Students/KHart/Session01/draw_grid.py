

def grid():
    corner = "+ "
    horiz = "- " * 4
    vert = "|"
    space = " " * 9
    

    horiz_edge = corner + horiz + corner + horiz + corner
    vert_edge = vert + space + vert + space + vert

    print horiz_edge
    for i in range(4):
        print vert_edge
    print horiz_edge
    for i in range(4):
        print vert_edge
    print horiz_edge


def print_grid(cell_width, columns, rows):
    corner = "+ "
    horiz = "- " * cell_width
    vert = "|"
    space = " " * (cell_width * 2 + 1)    
    
    horiz_edge = (corner + horiz) * columns + corner
    vert_edge = (vert + space) * columns + vert

    
    for i in range(rows):
        print horiz_edge
        for i in range(cell_width):
            print vert_edge
    print horiz_edge


print_grid(4, 3, 3)
