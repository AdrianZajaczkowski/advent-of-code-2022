# read file and separate by new line
with open('day1\elf_snack.txt') as f:
    trip = f.read().splitlines()


snack = []
elf = []
sums = []
sum_of_calories = 0

for i in range(len(trip)):
    if trip[i] != "":
        sum_of_calories += int(trip[i])
        snack.append(int(trip[i]))
        last = snack
    else:
        sums.append(sum_of_calories)
        elf.append(snack)
        snack = []
        sum_of_calories = 0

    if i == len(trip)-1:
        sums.append(sum_of_calories)
        elf.append(last)

# max sum_of_calories
result = [x for x in elf[171]]
print(sum(result))
print(sums.index(max(sums)))  # index of sum sum_of_calories
# sum of max 3
print(sum(sorted(sums)[-3:]))
