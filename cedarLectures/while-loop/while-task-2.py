#ask user for their name
#output all even positioned characters 
#then output all odd positioned characters

name = input("Please enter your name : ")
count = 0
evenstr = ''
oddstr = ''
for char in name:
    if (count % 2 == 0):
        evenstr = evenstr + char
    else:
        oddstr = oddstr + char
    count += 1

print(f"the odd positioned characters in your name are : {oddstr}")
print(f"the even positioned characters in your name are : {evenstr}")
