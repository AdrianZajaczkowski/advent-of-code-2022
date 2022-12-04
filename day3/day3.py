
from collections import Counter
with open('day3/rucksacks.txt') as f:
    rucksacks = f.read().splitlines()

sum = 0
sum2 = 0

# first part
# create dict with letters and value of letters
letters = {chr(i+96): i for i in range(1, 27)}  # lower letters

letter_higher = {chr(i+64): i+26 for i in range(1, 27)}  # upper letters
letters.update(letter_higher)  # dict of letters


for i in rucksacks:
    first_h = Counter(i[0:len(i)//2])
    second_h = Counter(i[len(i)//2:])
    result = first_h & second_h
    letter = list(set(result))[0]
    sum += letters[letter]
print(sum)

# second part. First step, create chunks with 3 elements
triplets = [rucksacks[i:i+3] for i in range(0, len(rucksacks), 3)]
for i in triplets:
    first = Counter(i[0])
    second = Counter(i[1])
    third = Counter(i[2])
    result = first & second & third
    letter = list(set(result))[0]
    sum2 += letters[letter]
print(sum2)
