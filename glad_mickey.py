from arena_fbf import *
"""
A gladiator's "turn" for FBF should be as follows

1. Check current room for needed conditions

2. FizzBuzz the room's int and submit number of Fizzes, Buzzes, and FizzBuzzes in order

3. If submission is correct, collect Macguffin

4. Move to new room

5. Repeat until all needed Macguffins are collected
"""
GLAD1 = "Mickey two-clicks"

import random

def fizzbuzz(number):
    fizz = 0
    buzz = 0
    fizzbuzz = 0
    for i in range(number):
        if i % 3 == 0 & i % 5 == 0:
            fizzbuzz += 1
        elif i % 3 == 0:
            fizz += 1
        elif i % 5 == 0:
            buzz += 0

    answer = [fizz, buzz, fizzbuzz]
    return answer

class Gladiator:
    def __init__(self, name, arena):
        # gladiator name
        self.name = name
        # arena size and info
        self.arena = arena
        self.row = random.randint(0, len(arena) - 1)
        self.col = random.randint(0, len(arena[0]) - 1)
        self.collected = set()

    def fizzbuzz(int):
        pass

    def move(self, direction):
        # moves based on u,d,l,r or cardinal directions
        if direction == "u" or "up" or "n" or "north" and self.row > 0:
            self.row -= 1
        elif direction == "d" or "down" or "s" or "south" and self.row < len(self.arena) - 1:
            self.row += 1
        elif direction == "l" or "left" or "w" or "west" and self.col > 0:
            self.col -= 1
        elif direction == "r" or "right" or "e" or "east" and self.col < len(self.arena) -1:
            self.col += 1

    def check_room(self):
        # returns arena location to gladiator
        return self.arena[self.row][self.col]
    
    def solve_room(self):
        room = self.check_room()
        # review room for conditions
        print(f"{self.name} is in a room with {room['macguffin']} with int {room['number']}.")
        
        #   if condition met, do action
        #   SPECIFICALLY CHECK SYNTAX BELOW FOR ACCURACY
        if room['macguffin'] not in self.collected:
            answer = fizzbuzz(room['number'])
            self.collected.append(self.submit(answer))
