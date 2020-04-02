


#총수입 = 수입-지출
price = 5.0
people = 120
before_total = 0
before_price = 0

while True :
    #수입 = 티켓의 가격 * 관객 수
    income = price * people

    #지출 = 고정비용 + (관객수 * 0.04)
    outcome = 180 + (people * 0.04)

    total = income - outcome

    if before_total > total :
        break
    else :
        before_total = total
        before_price = price

    price = price - 0.1
    people = people + 15

print(before_total)
print(before_price)
