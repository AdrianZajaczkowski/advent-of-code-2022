from copy import deepcopy
with open('day5/cargo.txt') as f:
    cargo = f.read().splitlines()


def createCraneGridFromData(cargo):
    grid = []
    for i in cargo:
        if len(i) == 0:
            break
        else:
            grid.append(i)
    return grid


def createStackFromGrid(grid):
    stacks_data = set(map("".join, zip(*reversed(grid))))
    stack_data = {}
    for i in stacks_data:
        if i[0].isnumeric():
            cranes = i[1:].split(" ")
            stack_data[int(i[0])] = list(cranes[0])
    return stack_data


def readMoves(cargo):
    index_of_empty_space = cargo.index('')
    moves = []
    jump = []
    for move in range(index_of_empty_space+1, len(cargo), 1):
        parts = cargo[move].split(' ')
        for part in parts:
            if part.isnumeric():
                jump.append(int(part))
        moves.append(jump)
        jump = []
    return moves


def moveCrates(moves, chunks, option):
    if option == 1:
        for move in moves:
            taking_data = chunks[move[1]][-move[0]:]
            chunks[move[1]] = chunks[move[1]][:-move[0]]
            chunks[move[2]] += taking_data[::-1]
        return chunks

    elif option == 2:
        for move in moves:
            taking_data = chunks[move[1]][-move[0]:]
            chunks[move[1]] = chunks[move[1]][:-move[0]]
            chunks[move[2]] += taking_data
    return chunks


grid = createCraneGridFromData(cargo)
moves = readMoves(cargo)
stack = createStackFromGrid(grid)
stack1 = deepcopy(stack)
stack2 = deepcopy(stack)

shuffle_stack1 = moveCrates(moves, stack1, 1)
shuffle_stack2 = moveCrates(moves, stack2, 2)
result = ''
for cranes, values in sorted(shuffle_stack1.items()):
    result += values[-1]
print("First part:", result)

result = ""
for cranes, values in sorted(shuffle_stack2.items()):
    result += values[-1]
print("Second part:", result)
