sum = int(input())

number_Petya = sum//6
number_Sergey = int(number_Petya)
number_Katya = int(number_Petya*4)

if(sum%6>0):
    print("Введена некорректная сумма")
else:
    print(f"Всего было сделано {sum}: Петя - {number_Petya}, Сережа - {number_Sergey}, Катя - {number_Katya}")



