myStr = "This is Cedar College"
print(myStr[5])
print(chr(65))
print(ord('a'))
print(len(myStr))

#[start : end]
#if left is empty : end = length
#if right is empty : end = length
#if left is negative : start = length - value
#if right is negative : end = length - value

#Mid
print(myStr[2:6])
print(myStr[0:5])

#Left
print(myStr[:5])
print(myStr[:-7])

#Right
print(myStr[14:])
print(myStr[-7:])

print(myStr.upper())
print(myStr.lower())

myNum = 7.99
print(int(myNum))
strNum = "7"
print(int(strNum))
strNum2 = "7.45"
print(int(float(strNum)))


