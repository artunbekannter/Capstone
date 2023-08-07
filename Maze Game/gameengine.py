from entities import Player, Wall, Exit
from maze import Maze, MazeLevel1, MazeLevel2, MazeLevel3
import time


# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣠⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣄⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠟⠛⠛⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠛⣷⡄⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡇⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡶⠀⠀⠀⠀⠀⠀⠀⢠⡀⠀⠀⢸⣧⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠛⠂⠀⠀⢰⠇⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠃⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠀⣰⣶⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡏⠀⠀⣀⣀⡀⠀⠀
# ⢀⣀⣀⣀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⢠⣦⠀⠀⠀⠀⢰⡇⠀⣿⠁⠀⠉⠻⣦⡀⠠⠟⠀⠀⠀⠀⣿⣧⣶⠿⠛⠙⣿⠀⠀
# ⣿⡋⠉⠙⠛⠷⣦⣄⠀⠀⣿⡇⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠈⠻⣦⣀⣀⣀⣀⣰⣿⠟⠁⠀⠀⠀⣿⠀⠀
# ⠸⣷⡀⠀⠀⠀⠈⠛⣷⡄⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠟⠀⠀⢸⣇⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⣿⡀⠀
# ⠀⠘⢿⣆⠀⠀⠀⠀⠈⢿⣿⡇⠀⠀⠀⠀⠀⠐⠟⠀⠀⠀⠀⡀⠀⢀⣴⡿⠃⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠙⣷⡄
# ⠀⠀⠀⠙⢷⣤⡀⠀⠀⠈⢿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢼⠇⠀⣼⡏⠀⠀⠀⠀⣾⣅⣀⣿⠀⠀⠀⠀⠀⠀⠀⣾⣅⢈⣷⠀⠀⠈⣿
# ⠀⠀⠀⠀⠀⠙⠿⣦⣀⠀⢸⡇⠀⠀⠀⠀⣰⡄⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠘⠻⠿⠟⠀⠀⠠⣖⢒⡶⠀⠙⠿⠿⠟⠀⠀⠀⣿
# ⠀⠀⠀⠀⠀⠀⠀⠈⠛⢷⣾⡇⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⢸⣧⠀⠀⠀⠀⠀⠀⢠⡄⠀⠀⠀⢈⣏⠀⠀⠀⠀⡀⠀⠀⠀⢀⣿
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣽⡇⠀⠀⠀⠀⠀⠠⡆⠀⠀⠀⢰⡆⠀⠀⢻⣧⡀⠀⠀⠀⠀⠈⠻⠶⣤⡴⠟⠙⠶⣤⡤⠞⠁⠀⠀⢀⣾⠏
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣻⣧⣄⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣙⣿⣶⣤⣄⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣤⣤⣶⠿⠋⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡟⠉⠉⠛⣿⠛⢻⠿⠿⠿⠿⣿⡿⠿⠛⠛⠛⠛⠛⣿⠛⠉⠙⠛⣿⠛⠛⣿⠟⠛⠛⢻⡏⠉⠉⠉⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣦⣀⣤⡾⠃⠀⣿⣀⣀⣠⣾⠟⠀⠀⠀⠀⠀⠀⠀⢿⣄⣀⣀⣴⠟⠀⠀⣿⠀⠀⢀⣾⠃⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀⠀⠈⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠁⠀⠀⠀⠙⠷⠶⠟⠃⠀⠀⠀⠀⠀⠀⠀⠀

# Nyan Cat music while writing comments for the longest part.

class GameEngine: # Well we need the class GameEngine, this is the brains, el jefe. The gameplay loop.
    def __init__(self, level_count = 3): # We have 3 levels from the Maze child class. So we have level_count = 3.
        self.level_count = level_count # The classes level count is the level_count specified.
        self.current_level = 1 # No way we start at level 1 :O
        self.levels = []
        self.player = None
    
    def load_levels(self):
        for level in range(1, self.level_count + 1):
            maze_class = globals()[f"MazeLevel{level}"] # So we are technically calling the MazeLevel child classes of maze. This makes the rest make sense.
            maze = maze_class() # Because maze = maze_class e.g MazeLevel1 we don't have to specify the class directly.
            maze.generate_maze() # So we're calling generate_maze from Maze class by proxy of MazeLevelNumber
            self.levels.append(maze) # Could we appending the list with the level? Yes I think so.
    
    def start_game(self):
        print(f"Welcome to Team E's Maze Runner.") # This is Team E's maze. Don't forget it.
        time.sleep(1)
        self.load_levels() # Michael Jackson had a song called Remember the Time. Here we remember the function above. Or well... The Python does.
        self.current_level = 1 # Current level = 1 but then we minus the 1 :O
        self.player = Player(self.levels[self.current_level - 1].start_x, self.levels[self.current_level - 1].start_y) # Finally we call the entity Player.
        self.play() # Well we've got what we need to let's male the game play! Function is below.
        
    def play(self):
        while self.current_level <= self.level_count:
            maze = self.levels[self.current_level - 1]
            
            self.create_maze(maze) # Well we do need to make the Maze class create a maze.
            
            move_direction = input(f"Enter a direction to move (W, A, S, D) or 'Q' to quit.\n") # People are lazy and used to games using W,A,S,D movement. Unless you like the original Tomb Raider games or early MS DOS games. Quick press alt to jump.
            
            # Also we are making the move_direction variable equal an input, it wouldn't be a good game if there wasn't user input.
            
            if move_direction.lower() == "q":
                break # It's sad, but sometimes we have to break things so they don't go on forever and ever and ever. Unless it's plastic or a radioactive isotope, then it goes on for a really long time.
            
            dx, dy = 0, 0
            if move_direction.lower() == "w":
                dy = -1 # You'll notice that we are just = here. Not +=. This is because our entity already does the adding.
            elif move_direction.lower() == "s": # Make sure you keep Y together and don't mix up a.
                dy = 1
            elif move_direction.lower() == "a": # Keep X together.
                dx = -1
            elif move_direction.lower() == "d":
                dx = 1
            
            # Insert joke about Generation X and Generation Y.
                
            self.player.move(dx, dy) # This is where we call it. Because this calculation exists in entities.py we don't really need to do the math again here.
            self.wall_collision(maze)
    
    def create_maze(self, maze):
        player_x, player_y = self.player.get_position() # Are we returning the position from the Player child class? Yes it returns here. And it also returns.
        maze.display_maze(player_x, player_y) # Well we want to display the maze and also position the player.
    
    def wall_collision(self, maze):
        if self.player.get_position() == (maze.exit_x, maze.exit_y): # Well if the player position returns equal values to the exit then the player has reached the exit.
            print(f"Congratulations! You have reached the exit.") # Insert sense of achievement dialogue.
            time.sleep(1)
            self.current_level += 1 # Add 1 to the current level.
            if self.current_level <= self.level_count:
                print(f"Next level...")
                time.sleep(1)
                self.player.x, self.player.y = maze.start_x, maze.start_y # Added to reset position on level. Same code as if wall is hit.
            else:
                print(f"Thanks for playing, you've done all 3 levels.") # Do you really want more levels to navigate than 3? It's the magic number. Yes it is.
        elif maze.maze[self.player.y][self.player.x] == 1: # Remember that 1 is a wall and 0 is an empty space. So if the player walks into a 1 then it's not a 1 it's a wall.
            print(f"You've collided with a wall. Try agin")
            time.sleep(1)
            self.player.x, self.player.y = maze.start_x, maze.start_y # Back to the beginning (start position).
        else:
            None
            
if __name__ == "__main__":
    game = GameEngine()
    game.start_game()