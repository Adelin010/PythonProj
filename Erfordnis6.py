#Domino with 2 numbers: ab, cd means b = c

def is_domino(num1: int, num2: int) -> bool:
    return (num1 % 10 == (num2//10) % 10)

def erford6(arr: list[int])-> tuple:
    l, l_max = 1, 0
    sol: list[int] = []
    temp: list[int] = [arr[0]]
    for idx in range(1, len(arr)):
        if is_domino(arr[idx-1], arr[idx]):
            l += 1
            temp[len(temp):] = [arr[idx]]
        else :
            if l > l_max:
                l_max = l
                sol = temp
            l = 1
            temp = [arr[idx]]

    if l > l_max:
        l_max = l
        sol = temp
    return (sol, l_max)

# print(erford6([12, 23, 34, 5, 65, 57, 78, 83, 39, 90]))