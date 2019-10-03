import gamemaster

player_colors = [
    [255, 0, 0],
    [0, 255, 0],
    [0, 0, 255]
]

master = gamemaster.Gamemaster(player_colors, 100, 100)

print(master.attack([0,0], [1,1], 6))
