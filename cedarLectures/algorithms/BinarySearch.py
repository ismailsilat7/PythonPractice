
#Array/List/Data must be sorted

List = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
SearchItem = input("Enter a character to search for: ").strip().upper()

def BinarySearch(SearchItem):
    Found = False
    SearchFailed = False
    First = 0
    MaxItems = len(List)
    Last = MaxItems - 1
    while not Found and not SearchFailed:
        Middle = int((First + Last)/2)
        if List[Middle] == SearchItem:
            Found = True
        else:
            if First >= Last:
                SearchFailed = True
            else:
                if List[Middle] > SearchItem:
                    # should be in first half
                    Last -= 1
                else:
                    # should be in second half
                    First += Middle
    if Found == True:
        return Middle
    else:
        return MaxItems + 1

try:
    index = BinarySearch(SearchItem)
    Item = List[index]
    print(f"{Item} found at index {index} (starting from 0) of array {List}")
except:
    print("Item not present in array")

