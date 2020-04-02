
min = 1
max = 100

while True:
    num = int((min + max) / 2)
    print(num)
    result = input("답을 입력하세요 :")
    if result == "C" :
        break
    if result == "H" :
        min = num
    elif result == "L" :
        max = num