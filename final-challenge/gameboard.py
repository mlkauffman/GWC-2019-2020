class Gameboard:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = {}
        x = 0
        while x < self.width:
            y = 0
            self.board[x] = []
            while y < self.height:
                self.board[x].append([0, 0])
                y = y + 1
            x = x + 1

    def get_space(self, x, y):
        return self.board[x][y]
        
    def set_space(self, x, y, details):
        self.board[x][y] = details
        
    def get_height(self):
        return self.height
        
    def get_width(self):
        return self.width
        
    def get_board(self):
        return self.board
        
    def change_space_owner(self, owner, x, y):
        self.board[x][y][0] = owner
        
    def set_space_units(self, units, x, y):
        self.board[x][x][1] = units
    
    def reduce_space_units(self, units, x, y):
        self.board[x][y][1] = self.board[x][y][1] - units
        
    def add_space_units(self, units, x, y):
        self.board[x][y][1] = self.board[x][y][1] + units