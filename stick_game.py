sticks = 21
while True:
    print("sticks left:", sticks)
    if sticks == 1:
        print("you lost the game")
        break
    stick_input = int(input("please input the number"))
    if stick_input >= 5 or stick_input <= 0:
        print("Wrong!")
        continue
    print("The computer took:", 5 - stick_input)
    sticks -= 51
