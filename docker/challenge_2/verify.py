import student_submission
import copy
import sys, os
import random

sys.stdout = open(os.devnull, "w")

weaknesses = {
    "Grass": ["Water", "Ground", "Rock"],
    "Rock": ["Fire", "Ice", "Flying", "Bug"],
    "Ice": ["Grass", "Ground", "Flying", "Dragon"],
    "Dragon": ["Dragon"],
    "Dark": ["Psychic", "Ghost"],
    "Psychic": ["Fighting", "Poison"],
    "Bug": ["Grass", "Psychic", "Dark"],
    "Flying": ["Grass", "Fighting", "Bug"],
    "Steel": ["Ice", "Rock", "Fairy"],
    "Fire": ["Grass", "Ice", "Bug", "Steel"],
    "Fighting": ["Normal", "Ice", "Rock", "Dark", "Steel"],
    "Ground": ["Fire", "Electric", "Poison", "Rock", "Steel"],
    "Ghost": ["Psychic", "Ghost"],
    "Poison": ["Grass", "Fairy"],
    "Water": ["Fire", "Ground", "Rock"],
    "Fairy": ["Fighting", "Dragon", "Dark"],
    "Electric": ["Water", "Flying"],
    "Normal": []
}

types = [
    'Grass',
    'Rock',
    'Ice',
    'Dragon',
    'Dark',
    'Psychic',
    'Bug',
    'Flying',
    'Steel',
    'Fire',
    'Fighting',
    'Ground',
    'Ghost',
    'Poison',
    'Water',
    'Fairy',
    'Electric',
    'Normal'
]

x = 0
good_answers = True
while (x < 50):

    player1 = random.choice(types)
    player2 = random.choice(types)

    student_result = student_submission.run(player1, player2)

    scoring_result = 0

    if player1 == player2:
        scoring_result = 3
    elif player2 in weaknesses[player1]:
        scoring_result = 1
    elif player1 in weaknesses[player2]:
        scoring_result = 2
    else:
        scoring_result = 3

    print(f"Player1: {player1}")
    print(f"Player2: {player2}")
    print("Student Result:")
    print(student_result)
    print("\nScoring Result:")
    print(scoring_result)
    if(student_result != scoring_result):
        good_answers = False
        break
    x = x + 1

sys.stdout = sys.__stdout__
if(good_answers):
    print("Victory!")
else:
    print("Defeat!")
