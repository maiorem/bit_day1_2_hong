import random

before = ""
win_count = 0

def game():
    user = int(input("가위 0 바위 1 보 2 \n"))
    com = random.randrange(0, 3)
    result = com - user
    result_str = ""
    if com < user :
        com = com + 3

    if result == 2 :
        result_str = "U"
    elif result == 1 :
        result_str = "C"
    else :
        result_str = "D"

    return result_str

while True:

    result = game()
    print("WINNER IS:", result)

    if result == "D" :
        win_count = 0

    if result == before :
        win_count = win_count + 1
    else :
        win_count = 1
        before = result

    if win_count == 3 :
        break
