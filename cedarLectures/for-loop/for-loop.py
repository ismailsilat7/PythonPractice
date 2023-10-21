# range excludes the last value
# range(s,e,i) end, start, increment
# range(s,e) i = +1 
# range(e) s = 0, i = +1

    

for x in range(2,14,3): 
    print(x, end=" ")
print()

for x in range(1,6):
    print(x, end = " meow ") #end replaces the default \n value
print()

for x in range(5):
    print(x, end= " ")
print()

for x in ["a", "b", "c", "d"]:
    print(x, end=" ")
print()
