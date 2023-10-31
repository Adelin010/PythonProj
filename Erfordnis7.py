# to find the smallest common multiple of a series of numbers we just need to 
# find the scm to two of them and then goes with the result to the next number and repeat the process

def SCM(num1: int, num2: int) -> int:
    prod = num1 * num2
    rest = num1 % num2
    while rest != 0:
        num1 = num2 
        num2 = rest 
        rest = num1 % num2
    
    return prod // num2

def erford7(array: list[int],* , start: int, stop: int) -> int:
    res: int = SCM(array[start], array[start+1])
    for number in array[start+2:stop+1]:
        res = SCM(res, number)
    
    return res


