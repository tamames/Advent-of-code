
def challenge_1()-> list:
    """This function computes the sum of all the calories carry by one elf"""

    add = 0
    amount_calories = []
    with open('amounts.txt', "r") as f:
        lines = f.readlines()

    for line in lines:
        if line !="\n":
            add += int(line)
        else:
            amount_calories.append(add)
            add = 0
    print(f"The greater amount of calories is {max(amount_calories)}")
    return amount_calories


def challenge_2(list_calories:list):
    sort_list = sorted(list_calories)
    amount = sum(sort_list[-3:])

    print(f"The amount of calories carried by the three top elfs is {amount}")
    

if __name__ == "__main__":
    amount = challenge_1()
    challenge_2(amount)

