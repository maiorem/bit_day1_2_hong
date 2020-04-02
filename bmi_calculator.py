
height = float(input("키는?"))
weight = int(input("체중은"))

bmi = weight / (height*height)

print(bmi)

if bmi < 18.5:
    print("저체중")
elif bmi < 23:
    print("정상")
elif bmi < 25:
    print("과체중")
else:
    print("비만")