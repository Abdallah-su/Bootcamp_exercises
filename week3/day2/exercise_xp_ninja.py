#board(world)
class game_of_life:
    def __init__(self, width, height):
        self.width = width
        self.height =height
        self.grid =[[0 for _ in range(width)] for _ in range(height) ]
        
#view
    def __str__(self):
        board_str = " "
        for row in self.grid:
            for cell in row:
                if cell == 0:
                    board_str += "."                                                                                                                                     
                else:
                    board_str += "#"
            board_str += "\n"
        return board_str
    
#    
    def toggle_cell(self, row, col):
        if self.grid[row][col] == 0:
            self.grid[row][col] = 1
        else: self.grid[row][col] = 0
            
    
# radar
    def count_live_neighbors(self, row, col):
        count_live = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                r_offst= row + i
                c_offset = col + j
                if i == 0 and j == 0:
                    continue
                if 0 <= r_offst <self.height and 0 <= c_offset <self.width:
                    if self.grid[r_offst][c_offset] == 1: 
                        count_live += 1
        return count_live             

# the time jump
    def new_board(self):
        new_grid = [[0 for _ in range(self.width)] for _ in range(self.height)]
        self.__str__()
        for r in range(self.height):
            for c in range(self.width):
                if self.grid[r][c] ==1 and 1 <self.count_live_neighbors(r, c) <=3 :
                     new_grid[r][c] = 1
                elif self.grid[r][c] == 0 and  self.count_live_neighbors(r,c) == 3:
                    new_grid[r][c] = 1
                else:new_grid[r][c] = 0
        self.grid = new_grid
import os
import time
my_game =game_of_life(10,10)  
my_game.toggle_cell(1,2)
my_game.toggle_cell(2,2)
my_game.toggle_cell(3,3)  
my_game.toggle_cell(5,7)   
my_game.toggle_cell(1, 5)
my_game.toggle_cell(5,2)
my_game.toggle_cell(6,6)
my_game.toggle_cell(6,5)
while True: 
     os.system('cls' if os.name == 'nt' else 'clear')
     my_game.new_board()
     print(my_game)
     time.sleep(0.5)
#Any live cell with fewer than two live neighbours dies, as if by underpopulation.
#Any live cell with two or three live neighbours lives on to the next generation.
#Any live cell with more than three live neighbours dies, as if by overpopulation.
#Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
