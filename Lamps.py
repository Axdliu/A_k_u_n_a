# -*- coding: utf-8 -*-
"""
Created on Wed Jan 04 12:37:18 2017

@author: User
"""

def num_illuminated(grid_width, grid_height, conn_x1, conn_y1, conn_x2, conn_y2, start_x, start_y):
    
    table = [(c,r) for c in range(grid_width) for r in range(grid_height)]
    lamps = {lamp : 1 for lamp in tuple(table)} 
    
    def lamp_off(lamps, start_x, start_y):         
        lamps[(start_x, start_y)] = 0        
        if (start_x + conn_x1, start_y + conn_y1) in lamps.keys():
            lamp_off(lamps, start_x + conn_x1, start_y + conn_y1)
        if (start_x + conn_x2, start_y + conn_y2) in lamps.keys():
            lamp_off(lamps, start_x + conn_x2, start_y + conn_y2)
    
    lamp_off(lamps, start_x, start_y) 
         
    return sum(lamps.values())
    
    
    
grid_width = 5
grid_height = 3
start_x = 4
start_y = 2
conn_x1 = -1
conn_y1 = 0
conn_x2 = -1
conn_y2 = -1

print num_illuminated(grid_width, grid_height, conn_x1, conn_y1, conn_x2, conn_y2, start_x, start_y)


def  num_illuminated(grid_width, grid_height, conn_x1, conn_y1, conn_x2, conn_y2, start_x, start_y):
    """
    grid_width - the width of the room grid
    grid_height - the height of the room grid
    conn_x1 - the x-coordinate of the first lamp connection
    conn_y1 - the y-coordinate of the first lamp connection
    conn_x2 - the x-coordinate of the second lamp connection
    conn_y2 - the y-coordinate of the second lamp connection
    start_x - the x-coordinate of the first lamp turned off
    start_y - the y-coordinate of the first lamp turned off
    """
    table = [(c,r) for c in range(grid_width) for r in range(grid_height)]
    lamps = {lamp:1 for lamp in tuple(table)}
    
    def lamp_off(lamps, x, y):
        if lamps[(x, y)] == 1:
            lamps[(x, y)] == 0
            if (x + conn_x1, y + conn_y1) in lamps.keys():
                lamp_off(lamps, x + conn_x1, y + conn_y1)
            if (x + conn_x2, y + conn_y2) in lamps.keys():
                lamp_off(lamps, x + conn_x2, y + conn_y2)
            
    lamp_off(lamps, start_x, start_y)
    
    return sum(lamps.values())