import random
from OSATools import *
from glad_mickey import *


ARENA = "FizzBuzz Fury"
MACGUFFINS = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple"]
ROWS = 5
COLUMNS = 5

# ARENA/GLADIATOR - BASIC IF/ELIF FIZZBUZZ
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

# ARENA - CREATES ROOMS WITH UNIQUE ARENA CHALLENGES
def create_room(macguffin, number):
    # Creates room with macguffin from list and number for fizzbuzz
    return {
        "macguffin" : macguffin,
        "number" : number,
        "fbcheck" : fizzbuzz(number)
    }

# ARENA/ENGINE - CREATES ARENA USING DEFINED ROOM RULES
# TODO - ?? create_arena(arena_specific) stays here
#           create_arena(todays_arena) should be used to call arena specific func
def create_arena(rows, cols):
    arena = [[create_room(random.choice(MACGUFFINS), random.randint(1000))
              for _ in range(cols)] for _ in range(rows)]
    return arena


def main():
    # OSA Arena intro, announces ARENA as competition and GLAD1, GLAD2 as competitors
    # TODO: MOVE ANNOUNCEMENT CALL TO MAIN ENGINE, CALL ANNOUNCEMENT FROM HERE
    osaannounce(ARENA, GLAD1, GLAD2)

    # Display rules/challenge for ARENA for contendors and observers
    intro = """
    FizzBuzz Fury!
    
    In the challenge ahead lies a grid full of rooms, each room containing a list of integers and labelled by a color
    
    You must navigate the rooms as efficiently as possible using Colors to find your way
    
    Differnet rooms will have different colors to identify the macguffin you receive when you finish that room's challenge
    
    To complete the challenge you will need to return the expected values in the order below:
            Fizzes (multiple of 3)
            Buzzes (multiple of 5)
            Fizzbuzzes (multiple of 3 and 5)
    Collect the correct Macguffins to find the exit and complete the challenge
    
    The first person that finishes with all required Macguffins is the winner!
    
    """

    # Load Arena and Gladiator files
    create_arena(ROWS, COLUMNS)

    # Place Gladiators in field
        # pick random XY point in arena to deposit - DONE IN GLAD.PY DURING INIT

    # Begin OSA Engine simulation loop
        # For each Gladiator
            # RUN GLADIATOR SCRIPT (E.G BELOW)
            # 1. searchRoom()
            # If neededMacguffin in room description
            #   a. FizzBuzz
            #   b. Submit response
            #   c. confirm positive, repeat or not
            # Else moveRoom()
        # If Gladiator.Victory() == True OR If Gladiator.noMoves() == True
        # Display winners
        
    return


if __name__ == "__main__":
    main()