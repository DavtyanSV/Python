array = input("Введите шестизначное число -> ")
first_number = int(array[:3:])
first_sum = (first_number%10 + (first_number//10)%10 + (first_number//10)//10)
second_number = int(array[3::])
second_sum = int(second_number%10 + (second_number//10)%10 + (second_number//10)//10)

if(first_sum==second_sum):
    print(f"{array} -> yes")
else:
    print(f"{array} -> no")
