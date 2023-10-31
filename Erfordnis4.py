# We will create a menu for operating with the encryption scheme
# for each symbol will be executed a different set of instruction for adding , multipling and XORing
# for the last will be supplied two methods : 1) that runs with the built-in operator ^ and one 
# manually created which compares two arrays of 1's and 0's

def XOR(dec1: int, dec2: int)-> int:
    binary1, binary2 = [], []

    #Binary interpretation of the numbers
    while dec1 != 0:
        binary1.append(dec1 % 2 )
        dec1 //= 2
    
    while dec2 != 0:
        binary2.append(dec2 % 2)
        dec2 //= 2
    
    #Equalizing the binary vectors
    len1 = len(binary1)
    len2 = len(binary2)
    if len1 > len2 :
        # Must be complete(fill it with 0's)
        for idx in range(len2, len1):
            binary2.append(0)
        len2 = len1
        
    elif len1 < len2:
        for idx in range(len1, len2):
            binary1.append(0)
        len1 = len2
        
    #to save memory the result will remain in binary2
    for idx in range(0, len1):
        if binary2[idx] == binary1[idx]:
            binary2[idx] = 0
        else :
            binary2[idx] = 1
    
    #Reconverting in base 10
    rez: int = 0
    for idx in range(0, len1):
        rez = rez + ((2 ** idx)*binary2[idx])
    
    return rez


# x = XOR(22, 2)
# print(x)


def erford4(arr: list[int], symbol: str)-> list[int]:
    rez = [arr[0]]
    match symbol:
        case "+":
            rez[len(rez):] = [arr[idx] + arr[0] for idx in range(1, len(arr))]
        case "*":
            rez[len(rez):] = [arr[idx] * arr[0] for idx in range(1, len(arr))]
        case "^":
            rez[len(rez):] = [arr[idx] ^ arr[0] for idx in range(1, len(arr))]
        case "XOR":
            rez[len(rez):] = [XOR(arr[idx], arr[0]) for idx in range(1, len(arr))]
        case _:
            raise TypeError("Symbol not accepted, a wrong symbol has been entered")
    return rez


# print(erford4([3, 12, 54, 34, 27, 87, 65, 67, 90], "+"))
# print(erford4([3, 12, 54, 34, 27, 87, 65, 67, 90], "*"))
# print(erford4([3, 12, 54, 34, 27, 87, 65, 67, 90], "^"))
# print(erford4([3, 12, 54, 34, 27, 87, 65, 67, 90], "XOR"))