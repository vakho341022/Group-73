# task 1

score = int(input("write your score: "))

if score >= 90 and score <= 100:
    print("your mark is: A")
elif score >= 80 and score <= 89:
    print("your mark is: B")
elif score >= 70 and score <= 79:
    print("your mark is: C")
elif score >= 60 and score <= 69:
    print("your mark is: D")
elif score >= 0 and score <= 59:
    print("your mark is: F")
else:
    print("this score doesn't exist!")



# task 2

num = int(input("write number to check: "))

if num > 0:
    print("this number is positive")
elif num < 0:
    print("this number is negative")
else:
    print("this number is 0")



# task 3

num1 = int(input("write first number: "))
num2 = int(input("write second number: "))

if num1 > num2:
    print("First Number is Greater than second one")
else:
    print("second Number is Greater than first one")



# task 4

number = int(input("write number to check: "))

if num % 2 == 0:
    print("this number is even")
else:
    print("this number is odd")



# task 5

temp = int(input("write temperature to check: "))

if temp < 0:
    print("Cold ❄️")
elif temp >= 0 and temp <= 30:
    print("Normal 🌤️")
else:
    print("Hot ☀️")