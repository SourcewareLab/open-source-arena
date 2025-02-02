# open-source-arena
Open Source Arena


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



****************************
* OSA ENGINE PROPOSED FLOW *
****************************
Load Arena and Gladiator files

Place Gladiators in field

Begin OSA Engine simulation loop

For each Gladiator
    RUN GLADIATOR SCRIPT (E.G BELOW)
    1. searchRoom()
        If neededMacguffin in room description
            a. FizzBuzz
            b. Submit response
            c. confirm positive, repeat or not
        Else moveRoom()
    If Gladiator.Victory() == True OR If Gladiator.noMoves() == True
        Display winners

***********************
* PROPOSED ARENA FLOW *
***********************
Define arena structure 
    Variable size grid (N by M)
    Define rooms (automtically or manually generated)
        FOR FIZZBUZZFURY SHOULD CONTAIN:
        
        Macguffin: Color
        Fizzbuzz: Integer
        Description: String including important details
        Allowed directions: U, D, L, R or N, E, S, W
    
    Handling Gladiator Actions
        Present room details
        Check for FizzBuzz response
        Check validation of submission
        Reward correct answers
        Check gladiator based on provided input?
        Check completion at end of "round"


***************************
* PROPOSED GLADIATOR FLOW *
***************************

Read Room
If conditions met
    Run script and submit answer

When collection is full > work towards goal and submit


**********************
SAMPLE ROOM IN DETAIL:
        Users will use conditions unique to rooms to find specific Macguffins
        Complete the room challenge to win the Specified MacGuffin
    
Room =    
    Name: Crystalline Sanctuary

    Desc: The walls of this room shimmer with various colored opaque crystalline structures\n
            Weaving through the crystals at the center of the room you find what appears to be a Blue Macguffin\n
            The Macguffin reflects the crystalline light behind a glass case secured with a FizzBuzz lock\n

    Note: This room provides an opportunity to throw a wrench into the process, the crystalline nature of the room\n
            might apply a color filter to the Macguffin to make it appear blue, but actually be another color\n
            to implement enhance description and add CONSISTENT FLAG OR STATEMENT to track tricks

    Contents: FizzBuzzChallenge(SizeVar, DiffVar), Blue Macguffin




