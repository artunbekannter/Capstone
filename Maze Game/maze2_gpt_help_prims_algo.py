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
        # Create a maze grid with all cells as walls
        self.maze = [[1 for _ in range(self.width)] for _ in range(self.height)]

        # Use Prim's algorithm to generate paths
        frontier = [(self.start_x, self.start_y)]
        self.maze[self.start_y][self.start_x] = 0

        while frontier:
            x, y = frontier.pop(random.randint(0, len(frontier) - 1))
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            random.shuffle(directions)

            for dx, dy in directions:
                nx, ny = x + dx * 2, y + dy * 2

                if 0 <= nx < self.width and 0 <= ny < self.height and self.maze[ny][nx] == 1:
                    self.maze[ny][nx] = 0
                    self.maze[y + dy][x + dx] = 0
                    frontier.append((nx, ny))

        # Add a border around the maze
        for y in range(self.height):
            for x in range(self.width):
                if x == 0 or x == self.width - 1 or y == 0 or y == self.height - 1:
                    self.maze[y][x] = 1

        # Make sure the start and exit positions are connected
        self.connect_start_exit()

    def connect_start_exit(self):
        # Check if the start and exit positions are already connected
        if self.is_connected(self.start_x, self.start_y, self.exit_x, self.exit_y):
            return

        # If not connected, find a path to connect them using simple BFS
        queue = [(self.start_x, self.start_y)]
        visited = set(queue)

        while queue:
            x, y = queue.pop(0)
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < self.width and 0 <= ny < self.height and self.maze[ny][nx] == 0 and (nx, ny) not in visited:
                    self.maze[ny][nx] = 0
                    queue.append((nx, ny))
                    visited.add((nx, ny))

                    # Check if the exit is adjacent to a path cell
                    if self.is_exit_adjacent(nx, ny):
                        return

            # If the exit is not adjacent to any path cell, choose a new random direction
            if not self.is_exit_adjacent(x, y):
                random.shuffle(directions)
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height and self.maze[ny][nx] == 0:
                        self.maze[ny][nx] = 0
                        queue.append((nx, ny))
                        visited.add((nx, ny))
                        break

    def is_exit_adjacent(self, x, y):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if nx == self.exit_x and ny == self.exit_y:
                return True
        return False

    def is_connected(self, x1, y1, x2, y2):
        # Check if two positions are connected using simple BFS
        queue = [(x1, y1)]
        visited = set(queue)

        while queue:
            x, y = queue.pop(0)
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if nx == x2 and ny == y2:
                    return True

                if 0 <= nx < self.width and 0 <= ny < self.height and self.maze[ny][nx] == 0 and (nx, ny) not in visited:
                    queue.append((nx, ny))
                    visited.add((nx, ny))

        return False
        
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
        super().__init__(width = 25, height = 25) # AMAZEing.
