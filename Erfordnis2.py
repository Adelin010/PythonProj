# for the symmetric of any number we just extract the digits from behind by dividing by 10 
# then add them each step multipling with 10 the previous result
# Then for this point of the project we return a lits of symmetrical numbers formed from the initial list

def Symmetrisch(num: int, cache: list[int]) -> int:
    if cache[num] != 0:
        #print("cached")
        return cache[num]
    
    copy: int  = num
    symm: int = 0
    if num == 0:
        return symm

    while num != 0:
        symm = symm * 10 + (num % 10)
        num //= 10
    
    cache[copy] = symm
    return symm

def erford2(array: list[int]) -> list[int]:
    freq = [0]*100
    res = [Symmetrisch(elem, freq) for elem in array]
    return res

# x = efrod2([12, 43, 12, 57, 24, 86, 34, 24, 18, 65])
# print(x)