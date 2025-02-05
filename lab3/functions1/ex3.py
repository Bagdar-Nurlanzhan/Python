def solve(numlegs, numheads):
    for rabbits in range(numheads + 1):
        chickens = numheads - rabbits
        if 2 * chickens + 4 * rabbits == numlegs:
            return chickens, rabbits
    return "No solution"
        
numheads = 35
numlegs = 94
result = solve(numlegs, numheads)
if result != "No solution":
    chickens, rabbits = result
    print( "chickens:" , chickens, "\nrabbits:" , rabbits)
else: 
    print(result)