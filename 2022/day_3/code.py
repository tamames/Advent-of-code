import string
from itertools import islice

PRIORITIES = dict()
for i, letter in enumerate(string.ascii_letters):
    PRIORITIES[letter] = i+1

def challenge1():
    with open('./2022/day_3/input.txt') as f:
        lines = f.readlines()

    sum_priorities = 0
    for line in lines:
        lengt = len(line)
        halve_1 = set(line[:lengt//2])
        halve_2 = set(line[lengt//2:])

        common = list(halve_1.intersection(halve_2))
        sum_priorities += PRIORITIES[str(common[0])]

    print(sum_priorities)
 



def challenge2():
    sum_priorities = 0
    with open('./2022/day_3/input.txt') as f:
        while True:
            groups = list(islice(f, 3))
            if not groups: 
                break
            elf_1 = set(groups[0].rstrip("\n")) #because of the intersection we only have to remove it once
            elf_2 = set(groups[1])
            elf_3 = set(groups[2])

            common = list(elf_1.intersection(elf_2, elf_3))
            sum_priorities += PRIORITIES[str(common[0])]

    print(sum_priorities)


if __name__ == '__main__':
    challenge1()
    challenge2()