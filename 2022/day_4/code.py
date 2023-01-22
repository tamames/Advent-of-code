
def check_overlap_1(elf_1: list[str], elf_2: list[str]) -> bool:

    elf_1 = list(map(int, elf_1))
    elf_2 = list(map(int, elf_2))

    if elf_1[0] <= elf_2[0] and elf_1[1] >= elf_2[1]: #if elf_2 is inside elf_1
        return True
    if elf_1[0] >= elf_2[0] and elf_1[1] <= elf_2[1]: #if elf_1 is inside elf_2
        return True
    
    return False


def challenge1():
    with open('./2022/day_4/input.txt') as f:
        lines = f.read().splitlines()
    
    overlaps = 0
    for line in lines:
        elf_1, elf_2 = line.split(",")
        if check_overlap_1(elf_1.split("-"), elf_2.split("-")):
            overlaps += 1
    
    print(overlaps)


def check_overlap_2(elf_1: list[str], elf_2: list[str]) -> bool:

    elf_1 = list(map(int, elf_1))
    elf_2 = list(map(int, elf_2))

    if elf_1[0] > elf_2[1]:
        return False

    return elf_1[1] >= elf_2[0]
        

def challenge2():
    with open('./2022/day_4/input.txt') as f:
        lines = f.read().splitlines()

    overlaps = 0
    for line in lines:
        elf_1, elf_2 = line.split(",")
        if check_overlap_2(elf_1.split("-"), elf_2.split("-")):
            overlaps += 1

    print(overlaps)


if __name__ == '__main__':
    challenge1()
    challenge2()