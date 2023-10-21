#take 2 numbers as inout and add them together. output the final answer.
#int() is used to cast string as integers

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

sum = num1 + num2

print(sum)

print("Your Number is:", num1, ", My number is:", num2)

print("Your Number is: {1}, My number is: {0}".format(num1,num2))