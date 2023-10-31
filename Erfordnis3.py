#So to speak the biggest number formed from the concatenation of all the number within the list
# it's just the number formed with all the numbers in descending order
# although easy for 2digit-numbers, for the purpose of learning, a quick sort will be implemented
# The Compare() is needed because if we have let's say: [123, 97] than the result of 12397 is less then 97123
# So the simple Descending sorting works only for numbers formed from the same number of digits
# The compare function has a simple logic >0 when num1 > num2 | <0 num1 < num2 | =0 when num1 = num2

def Swap(arr: list, poz1: int, poz2: int):
    temp = arr[poz1]
    arr[poz1] = arr[poz2]
    arr[poz2] = temp

def Compare(num1: int, num2: int) -> int:
    ogl1, ogl2 = 0, 0
    while num1 != 0:
        ogl1 = ogl1 * 10 + (num1 % 10)
        num1 //= 10
    while num2 != 0:
        ogl2 = ogl2 * 10 + (num2 % 10)
        num2 //= 10
    
    while ogl1 != 0 or ogl2 != 0:
        if ogl1 % 10 > ogl2 % 10:
            return 1
        elif ogl1 % 10 < ogl2 % 10:
            return -1
        ogl1 //= 10
        ogl2 //= 10
    
    if ogl1 != 0 and ogl2 == 0:
        return 1
    if ogl1 == 0 and ogl2 != 0:
        return -1
    return 0
        

def Partition(array: list[int], start: int, stop: int) -> int :
    pivot = array[stop]
    idx: int = start - 1

    for index in range(start, stop+1):
        if Compare(array[index], pivot) == 1:
            idx += 1
            Swap(array, idx, index)
    
    Swap(array, idx+1, stop)
    return idx+1


def quickSort(*, array: list[int], start: int, stop: int) -> None:
    if start >= stop:
        return
    pivot_idx = Partition(array, start, stop)
    quickSort(array=array, start=start, stop=pivot_idx - 1)
    quickSort(array=array, start=pivot_idx + 1, stop=stop)

def erford3(array: list[int]):
    quickSort(array=array, start= 0, stop= len(array)-1)
    return("".join([str(elem) for elem in array]))

# erford3([12, 4, 23, 5 ,765, 3, 6, 234, 54, 67, 86, 35, 3, 45, 32, 46,785])
