with open('day4/camp.txt') as f:
    camp = f.read().splitlines()
# print(camp)
elf_pairs = []
for i in camp:
    step1 = i.split(',')
    tmp1 = step1[0].split('-')
    tmp2 = step1[1].split('-')
    # print([tmp1,tmp2])
    elf_pairs.append([list(map(int, tmp1)), list(map(int, tmp2))])

# 1 & 2 tasks
fully_contains = 0
for pair in elf_pairs:
    # start and end of each range from current elves pair
    start_1 = pair[0][0]
    end_1 = pair[0][1]
    start_2 = pair[1][0]
    end_2 = pair[1][1]
    # +1 bcs range() end 1 before current number so to get full range, i add 1 to the end of range
    range1 = range(pair[0][0], pair[0][1]+1)
    range2 = range(pair[1][0], pair[1][1]+1)

    # to get answer in 1 task use and, to get result of second task: use or in if statment
    if start_1 in range2 or end_1 in range2:
        fully_contains += 1
    elif start_2 in range1 or end_2 in range1:
        fully_contains += 1
print(fully_contains)
