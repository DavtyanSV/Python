number = int(input("Введите трехзначное число -> "))


result = int(number%10 + (number//10)%10 + (number//10)//10)

print(result)