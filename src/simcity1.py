'''
Created on Nov. 9, 2023
Receives a text file and returns it formatted as a grid of values
@author: Sebastian
'''

def create_grid(filename):
    """
    Create a grid of land values from a file
    eg. 2
        2
        1
        2
        3
        4
        would return [[1,2],[3,4]]
    """
    map = []
    
    file = open(filename, "r")
    tile_list = file.readlines()
    numRow = int(tile_list[0])
    colRow = int(tile_list[1])
    for row in range(numRow) :
        map.append([0]*colRow)
        for col in range(colRow) :
            value = tile_list[((row*numRow)+col)+2] #the + 2 skips the row and column valuation. The row*4 accounts for the fact that simply adding row and col would repeat values
            map[row][col] = int(value) #removes the new line character
    return map

def display_grid(grid):
    """
    Display a grid of land values
    eg. [[1,2],[3,4]]
    would return 
    1    2
    3    4
    """
    for row in grid :
        for col in row:
            print(f"{col:9}",end="")
        print() #newline character at the end of each row


def main():
    """
    Main program.
    """
    grid = create_grid("data_1.txt")
    print("SimCity Land Values:")
    display_grid(grid)
    
if __name__ == "__main__" :
    main()