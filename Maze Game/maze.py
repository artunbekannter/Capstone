import sys, os, random

def clscon(): #Defining a function that clears the terminal "clscon" for clear console. We can actually do this with os.system paramaters having an if statements rather than a convoluted longer function (as you can see highlighted out below).
    os.system('cls' if os.name == 'nt' else 'clear') #Basic IF statement, if the OS is 'NT' we use 'cls' to clear, if it's Posix we use 'clear'.

class Maze():
    def __init__(self, width, height):
        # We need the maze to have dimensions, so we have to have width and height.
        self.width = width 
        self.height = height
        self.maze = [] # This is empty because we make it into the layout. At present we haven't generated a maze until we generate_maze().
        self.start_x, self.start_y  = 1, 1 # So we have a starting point for where the player starts.
        self.exit_x, self.exit_y = width - 2, height - 2 # So we have an exit point for where the exit is. - 2 is so that we keep it away from the exact edge of the maze.
        
    def generate_maze(self):
        self.maze = [[0 for _ in range(self.width)] for _ in range (self.height)] # We are generating the layout for the maze, 0 would be each block of maze.
        
        # To make it easier to visualise this... Width is lists within a height list. [0, 0, 0] so width 3 in this case.
        
        #[
        #[0, 0, 0]   y
        #[0, 0, 0] x x x
        #]           y
        
        #So above it would be width 3, height 2.
        
        self.maze[self.start_y][self.start_x] = 0 # Start position of player.
        self.maze[self.exit_y][self.exit_x] = 0 # Exit position of maze.
        
        
        # I do not get credit for this solution. It was Chat GPT that helped figure out the borders.
        for x in range(self.width):
            self.maze[0][x] = 1
            self.maze[self.height - 1][x] = 1 
        for y in range(self.height):
            self.maze[y][0] = 1 
            self.maze[y][self.width - 1] = 1
        
        num_walls = int(0.3 * self.width * self.height) # We are adding a 0.3 (or 30% generation) of walls.
        for _ in range(num_walls): # We're making a loop, it iterates this loop based on the num_walls calculation.
            x, y = random.randint(0, self.width -1), random.randint(0,self.height -1) # We are using random integers to generate places within the maze where there will be a wall. We are -1 so that we don't cause the location x, y to go outside of the maze.
            self.maze[y][x] = 1 # This is just basically that if the maze space is 0 then the wall is 1.
        
    def display_maze(self, player_x, player_y):
        clscon()
        for y in range(self.height): # For the vertical
            for x in range(self.width): # For the horizontal
                if x == self.start_x and y == self.start_y:
                    print("S", end = " ") # If the x and y = we are printing S.
                elif x == self.exit_x and y == self.exit_y:
                    print("E", end = " ") # Same.
                elif x == player_x and y == player_y:
                    print("P", end = " ") # No way, me too!
                else:
                    # print(str(self.maze[y][x]), end = " ")
                    print(" " if self.maze[y][x] == 0 else "#", end = " ") # There's probably a way to use the Wall entity here, but because it's already simply generated we can just say if it isn't 0 (so it's 1 which is a wall) then print #.
            print()
        

# def main():
#     print(f"Test")
#     maze = Maze(15, 15)
#     maze.generate_maze()
#     maze.display_maze()
#     print()
    
# if __name__ == "__main__":
#     main()

class MazeLevel1(Maze):
    def __init__(self):
        super().__init__(width = 10, height = 10) # So basically these child classes just define the size of the generation. So level 1 is 10 by 10.

class MazeLevel2(Maze):
    def __init__(self):
        super().__init__(width = 15, height = 15) # Is level 2 15 by 15? Yes it is.

class MazeLevel3(Maze):
    def __init__(self):
        super().__init__(width = 20, height = 20) # AMAZEing.
