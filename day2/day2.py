with open('day2/r_p_s.txt') as f:
    game = f.read().splitlines()
rounds = []
for i in game:
    round = i.split(" ")
    rounds.append(round)
# A - rock, B - paper, C - scisors
# X - rock 1p, Y - paper 2p, Z - scisors 3p

points = {'X': 1,
          'Y': 2,
          'Z': 3,
          'A': 1,
          'B': 2,
          'C': 3,
          }

# first part
# lists for compare letters to pattern

draws = [['A', 'X'], ['B', 'Y'], ['C', 'Z']]
won_rounds = [['C', 'X'], ['A', 'Y'], ['B', 'Z']]
lose_rounds = [['A', 'Z'], ['B', 'X'], ['C', 'Y']]

sum_options = 0
for i in rounds:
    if i in draws:
        sum_options += 3
    elif i in won_rounds:
        sum_options += 6
    elif i in lose_rounds:
        pass
    sum_options += points[i[1]]
print(sum_options)

# part 2
# create list of patterns and list with results when specific character occurs
draws = [[['A', 'Y'], ['B', 'Y'], ['C', 'Y']],
         [['A', 'A'], ['B', 'B'], ['C', 'C']]]

lose_rounds = [[['C', 'X'], ['A', 'X'], ['B', 'X']],
               [['C', 'B'], ['A', 'C'], ['B', 'A']]]

won_rounds = [[['A', 'Z'], ['B', 'Z'], ['C', 'Z']],
              [['A', 'B'], ['B', 'C'], ['C', 'A']]]

sum_options2 = 0
for i in rounds:
    if i[1] == "X":
        sum_options2 += 0
        pos = lose_rounds[0].index(i)
        letter = lose_rounds[1][pos][1]

    elif i[1] == "Y":
        sum_options2 += 3
        pos = draws[0].index(i)
        letter = draws[1][pos][1]

    elif i[1] == "Z":
        sum_options2 += 6
        pos = won_rounds[0].index(i)
        letter = won_rounds[1][pos][1]
    sum_options2 += points[letter]
print(sum_options2)
