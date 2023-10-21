#keep asking user until user enters 0
#for all even numbers entered add them to the total
#for all odd numbers entered minus them from the total
#for all prime numbers multiply them with the final answer
#output the final answer
print("enter '0' to stop the loop")
primelist = []
num = int(input("Please enter a number : "))
total = 0
while (num != 0):
    if (num % 2 == 0):
        total += num
    else:
        total -= num
    if (num > 2):
        divide_count = 0
        for i in range(2, int(num**0.5) + 1):
            if (num % i == 0):
                divide_count += 1
                break
        if(divide_count == 0):
            primelist.append(num)
    if (num == 2):
        primelist.append(num)
    num = int(input("Please enter a number : "))

for num in primelist:
    total *= num

print(primelist)


print(f"The total is : {total}")
