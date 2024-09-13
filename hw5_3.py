# exercise 1
height: float = float(input("Enter your height in meters: "))

while height < 0.4 or height > 2.5:
    print("Wrong input")
    height = float(input("Enter your height in meters: "))

# exercise 2
a: int = int(input("Enter a number: "))
b: int = int(input("Enter a number: "))

if a < b:
    for a in range(a, b + 1, 1):
        print(a, end=" ")
else:
    for a in range(a, b - 1, -1):
        print(a, end=" ")
print()

# exercise 3
counter: int = 1
pie: float = float(input("What is the 'pie' number equals to? "))

while pie < 3.14 or pie > 3.14 and counter < 3:
    counter += 1
    pie: float = float(input("What is the 'pie' number equals to? "))

if counter == 4:
    print("Pie is 3.14")
else:
    print("You are correct")
print()

# exercise 4
while True:
    num1: int = int(input("Enter a number: "))
    num2: int = int(input("Enter a number: "))
    num3: int = int(input("Enter a number: "))
    sum_numbers = num1 + num2 + num3
    avg_numbers = sum_numbers / 3
    is_valid_num1 = 0 <= num1 <= 10
    is_valid_num2 = 10 <= num2 <= 60
    is_valid_num3 = 60 <= num3 <= 100
    if is_valid_num1 and is_valid_num2 and is_valid_num3 and num2 == avg_numbers:
        break

# STOP
