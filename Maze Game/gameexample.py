

class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.maze_layout = []
        self.start_x, self.start_y = 1, 1
        self.exit_x, self.exit_y = width -2, height -2
        
        
class MazeLevel1:
    def __init__(self):
        super().__init__(width = 10, height = 10)
        
class MazeLevel2:
    def __init__(self):
        super().__init__(width = 15, height = 15)
        
class MazeLevel3:
    def __init__(self):
        super().__init__(width = 20, height = 20)





class GameEntity:
    def __init__(self, x, y, symbol):
        self.x = x
        self.y = y
        self.symbol = symbol
        
class Player(GameEntity):
    def __init__(self, x, y):
        super().__init__(x, y, "P")
        
class Wall(GameEntity):
    def __init__(self, x, y):
        super().__init__(x, y, "#")
        
class Exit(GameEntity):
    def __init__(self, x, y):
        super().__init__(x, y, "E")
        
        
        
        
        
        
        
class GameEngine:
    def __init__(self, maze):