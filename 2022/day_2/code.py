
with open("./2022/day_2/input.txt") as f:
    lines = f.readlines()

points = 0
awarded_points = {"X": 1, "Y":2, "Z":3}
match = {
    ("A", "Z"): 0, ("B", "X"): 0, ("C", "Y"): 0,
    ("A", "X"): 3, ("B", "Y"): 3, ("C", "Z"): 3,
    ("A", "Y"): 6, ("B", "Z"): 6, ("C", "X"): 6
}

for line in lines:
    opponent, me = line.split()

    points += awarded_points[me]
    points += match[(opponent,me)]

print(points)

    

    
