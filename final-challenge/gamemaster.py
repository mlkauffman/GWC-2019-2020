from player import Player
from gameboard import Gameboard
import random


class Gamemaster:

    def __init__(self, player_colors, board_width, board_height):
        self.players = []
        curr_id = 0
        for color in player_colors:
            new_player = Player(color, curr_id, 0, 0)
            curr_id = curr_id + 1
            self.players.append(new_player)
        self.board = Gameboard(board_width, board_height)
        x = 0
        while x < self.board.get_width():
            y = 0
            while y < self.board.get_height():
                selection = random.sample(self.players, 1)
                self.board.set_space(x, y, [selection[0].get_id(), 5])
                y = y + 1
            x = x + 1
            
    def get_board(self):
        return self.board.get_board()
        
    def attack(self, source_coords, target_coords, max_attackers):
        if len(source_coords) != 2:
            return -1
        if len(target_coords) != 2:
            return -2
        if source_coords[0] < 0:
            return -3
        if source_coords[0] >= self.board.get_width():
            return -4
        if source_coords[1] < 0:
            return -5
        if source_coords[1] >= self.board.get_height():
            return -6
        if target_coords[0] < 0:
            return -7
        if target_coords[0] >= self.board.get_width():
            return -8
        if target_coords[1] < 0:
            return -9
        if target_coords[1] >= self.board.get_height():
            return -10
        if abs(target_coords[0] - source_coords[0]) > 1:
            return -11
        if abs(target_coords[1] - source_coords[1]) > 1:
            return -12
        if self.board.get_space(source_coords[0], source_coords[1])[0] == self.board.get_space(target_coords[0], target_coords[1])[0]:
            return -13
        if self.board.get_space(source_coords[0], source_coords[1])[1] <= max_attackers:
            return -14
            
        defender_casualties = 0
        max_defenders = self.board.get_space(target_coords[0], target_coords[1])[1]
        attacker_casualties = 0
        
        while(attacker_casualties < max_attackers) and (defender_casualties < max_defenders>):
            curr_attackers = 3
            curr_defenders = 2
            defender_rolls = []
            attacker_rolls = []
            if (max_attackers - attacker_casualties) < 3:
                curr_attackers = max_attackers - attacker_casualties
            if (defender_casualties - max_defenders) < 2:
                curr_defenders = defender_casualties - max_defenders
                
            x = 0
            while(x < curr_attackers):
                attacker_rolls.append(random.randint(1, 6))
                x = x + 1
            x = 0
            while(x < curr_defenders):
                defender_rolls.append(random.randint(1, 6))
                x = x + 1
            
            y = 0
            attacker_rolls.sort(reverse=True)
            defender_rolls.sort(reverse=True)
            if len(attacker_rolls) > len(defender_rolls):
                y = len(attacker_rolls)
            else:
                y = len(defender_rolls)
                
            x = 0
            while (x < y):
                if attacker_rolls[x] > defender_rolls[x]:
                    defender_casualties = defender_casualties + 1
                else:
                    attacker_casualties = attacker_casualties + 1
            
        if attacker_casualties == max_attackers:
            print "Attacker lost"
            //todo
            
        if defender_casualties == max_defenders:
            print "Defender lost"
            //todo
        
        random.randint(1, 6)
        
        
        return 1