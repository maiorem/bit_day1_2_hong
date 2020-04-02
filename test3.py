from random import randrange

value = randrange(0, 4)
current = 0

while True:
    input("ENTER 누르기")

    print(current, value)

    if current == value :
        print("커피쏘기")
        break
    else:
        print("얻어먹기")

    current = current + 1