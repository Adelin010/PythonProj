#This function returns a new list of integers, whose appearances have a frequency of 1
# The frequency array is by default initialised with -1(not in the list)
# When find for the first time - let's say number n - freq[n] = 1 
# if the previous number n is found once more than it's frequency is set to 0 (freq[n] = 0)
# in the returned list will be placed only those elems whose freq[x] = 1, whatsoever x = 10,...,100


def erford1(array: list[int])-> list[int]:
    freq = [-1] * 100
    for elem in array:
        if freq[elem] == -1:
            freq[elem] = 1
        elif freq[elem] == 1:
            freq[elem] = 0

    return [index for index in range(0, len(freq)) if freq[index] == 1]    


# x = erfor1([12, 23, 43, 56, 34, 23, 56, 23, 24, 25, 78, 89, 96, 95, 67, 65, 45])
# print(x)