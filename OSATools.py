from time import sleep
from arena_fbf import *
from glad_mickey import *


GLAD2 = "Absolute Zero Zane"

def osaannounce(arena, glad1, glad2):
    announcements = [
        "Open Source Arena",
        "Created as by Sourceware Labs",
        f"Today's challenge is: {arena}",
        f"Contendors for this match are {glad1} and {glad2}"
    ]

    for announce in announcements:
        print(announce)
        sleep(1)

def run_game():
    rows, cols = 3, 3 # set arena size
    arena = create_arena(rows, cols)
    # GLAD1 to create gladiator comes from gladiator file
    # pulls functions user writes as methods atm
    # separate this out per-room movements is part of GLAD function instead of built here
    mickey = Gladiator(GLAD1, arena)

    print ("Game Start!\n")

    # NOTE: THIS IS CURRENTLY ONLY WORKING FOR A SINGULAR GLADIATOR
    # TODO: BUILD ENGINE OUT - Interact with both gladiators instead of just mickey
    #       Have engine check each "tick" with gladiators for completed list
    #       Move this loop to gladiator file
    #       This should check gladiators for completion, then tick forward

    while len(mickey.collected) < len(MACGUFFINS):
        mickey.solve_room()
        mickey.move(random.choice(["up", "down", "left", "right"]))

    print(f"Game Over! {GLAD1} has completed the challenge")


    if __name__ == "__main__":
        run_game()
