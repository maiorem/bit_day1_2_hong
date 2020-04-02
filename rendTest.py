
import random



while True :

    user = int(input("가위 0, 바위 1, 보 2 \n"))
    com = random.randrange(0, 3)

    if com < user:
        com = com + 3

    result = com - user
    result_str = ""

    if result == 2:
        result_str = 'WIN'
    elif result == 1:
        result_str = 'LOSE'
    else:
        result_str = 'DRAW'

    print(result_str)


