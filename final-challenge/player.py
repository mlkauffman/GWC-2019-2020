class Player:

    def __init__(self, color, id, total_units, total_spaces):
        self.color = color
        self.id = id
        self.tsotal_units = total_units
        self.total_spaces = total_spaces
        
    def get_color(self):
        return self.color
        
    def set_color(self, color):
        self.color = color
        
    def get_id(self):
        return self.id
        
    def set_id(self, id):
        self.id = id
        
    def get_total_units(self):
        return self.total_units
        
    def set_total_units(self, total_units):
        self.total_units = total_units
        
    def get_total_spaces(self):
        return self.total_spaces
        
    def set_total_spaces(self, total_spaces):
        self.total_spaces = total_spaces
        
    def add_units(self, units):
        self.total_units = self.total_units + units
        
    def reduce_units(self, units):
        self.total_units = self.total_units - units
        
    def add_spaces(self, spaces):
        self.total_spaces = self.total_spaces + spaces
        
    def reduce_spaces(self, spaces):
        self.total_spaces = self.total_spaces - spaces