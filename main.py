total_price =0
count_ticket = int(input('Введите количество билетов'))
if count_ticket > 3:
    discount = 10
else:
    discount = 0
for i in range(count_ticket) :
    age = int(input('age ='))
    if age < 18 :
        price_ticket = 0
    elif 18 <= age <= 25 :
        price_ticket = 990
    else:
        price_ticket = 1390
    total_price += price_ticket
print('Общая стоимость билетов = ', total_price, 'руб')
if discount :
    total_price*=(100-discount)/100
    print(f"Ваша скидка = {discount} %. Итоговая цена ={total_price}, руб")
