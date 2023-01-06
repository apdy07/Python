# Write your code here.

# You'll have to use the following strings:
# 1) "Enter a number: "
# 2) "Enter another number: "
# 3) "The sum of these two numbers is:"
# 4) "That is a large sum!"

num = float(input("Enter a number: "))
if num>=10 and num<20:
    num1 = float(input("Enter another number: "))
    sum = num+num1
    print("The sum of these two numbers is:" ,sum)
    if sum>100:
        print("That is a large sum!")
