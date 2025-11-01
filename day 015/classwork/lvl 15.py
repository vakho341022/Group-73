# task 1

# == - ოპერატორი გამოიყენება როდესაც უნდა შევადაროთ მაგ. ორი ცვლადი ერთმანეთს, არიან თუ არა ერთმანეთის ტოლი და პასუხს ვიღებთ boolean-ის სახით
print("vakho" == "10")
print("vakho" == 20)
print(50 == "10")
print(100 == 100)
print(0 == -1)
# != - ოპერატორი გამოიყენება როდესაც უნდა შევადაროთ მაგ. ორი ცვლადი ერთმანეთს, არ არიან თუ არიან ერთმანეთის ტოლი და პასუხს ვიღებთ boolean-ის სახით
print("12" != 12)
print("num" != 14)
print("num" != "num")
print(17 != 12)
print(22 != 22)


# task 2

# Conditional Statement — პირობითი განცხადება არის ისეთი კოდის ნაწილი, რომელიც ასრულებს სხვადასხვა მოქმედებას დამოკიდებულად იმაზე, არის თუ არა მოცემული პირობა ჭეშმარიტი თუ მცდარი

# Python-ში პირობითი განცხადებისთვის გვაქვს 3 keyword-ი:
# 1. if – "თუ"
# 2. elif – "სხვა შემთხვევაში თუ"
# 3. else – "სხვა შემთხვევაში"


# task 3

age = int(input("write your age: "))

if age > 18:
    print("you are an adult!")
elif age == 18:
    print("you are 18yo!")
else:
    print("you are teenager!")


# task 4

num = 1

while num < 5:
    print("vakho")
    num += 1


# task 5

for i in range(1, 6):
    i += i
    print(i)


# task 6

name1 = str(input("write your name: "))
name2 = "vakho"

if name1 == name2:
    print("the names are same")
else:
    print("the names are different")