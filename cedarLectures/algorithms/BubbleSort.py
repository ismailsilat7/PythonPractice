
List = ["E", "C", "A", "B", "D"]
def BubbleSort():
    global List
    MaxIndex = len(List)
    n = MaxIndex - 1
    for i in range(MaxIndex):
        for j in range(n):
            if List[j] > List[j+1]:
                Temp = List[j]
                List[j] = List[j+1]
                List[j+1] = Temp
        n = n - 1

print(List)
BubbleSort()
print(List)