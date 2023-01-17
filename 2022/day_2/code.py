
def challenge1() -> None:

    with open("./2022/day_2/input.txt") as f:
        lines = f.readlines()

    points = 0
    match = {
        ("A", "Z"): 3, ("B", "X"): 1, ("C", "Y"): 2,
        ("A", "X"): 4, ("B", "Y"): 5, ("C", "Z"): 6,
        ("A", "Y"): 8, ("B", "Z"): 9, ("C", "X"): 7
    }

    for line in lines:
        opponent, me = line.split()
        points += match[(opponent,me)]

    print(points)

def challenge2() -> None:

    with open("./2022/day_2/input.txt") as f:
        lines = f.readlines()

    points = 0
    match = {
        ("A", "Z"): 8, ("B", "X"): 1, ("C", "Y"): 6,
        ("A", "X"): 3, ("B", "Y"): 5, ("C", "Z"): 7,
        ("A", "Y"): 4, ("B", "Z"): 9, ("C", "X"): 2
    }

    for line in lines:
        opponent, me = line.split()
        points += match[(opponent, me)]

    print(points)

if __name__ == "__main__":
    challenge1()
    challenge2()


    

    
