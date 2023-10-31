from Erfordnis1 import erford1 as task1
from Erfordnis2 import erford2 as task2
from Erfordnis3 import erford3 as task3
from Erfordnis4 import erford4 as task4
from Erfordnis5 import erofrod5 as task5
from Erfordnis6 import erford6 as task6
from Erfordnis7 import erford7 as task7



class SysMeniu:
    
    def __init__(self, array: list[int], exe_op: int) -> None:
        self.array = array
        self.exe_op = exe_op

    def setExeOp(self, exe_op):
        self.exe_op = exe_op
    
    def Exe(self):
        match self.exe_op:
            case 1:
                SysMeniu.erfordnis1(self.array)
            case 2:
                SysMeniu.erfordnis2(self.array)
            case 3:
                SysMeniu.erfordnis3(self.array)
            case 4:
                SysMeniu.erfordnis4(self.array)
            case 5:
                SysMeniu.erfordnis5(self.array)
            case 6:
                SysMeniu.erfordnis6(self.array)
            case 7:
                SysMeniu.erfordnis7(self.array)


    def erfordnis1( arr:list[int]) -> None:
        print(task1(arr))

    def erfordnis2( arr:list[int]) -> None:
        print(task2(arr))

    def erfordnis3(arr:list[int]) -> None:
        print(task3(arr))

    def erfordnis4( arr:list[int]) -> None:
        print("With +")
        print(task4(arr, "+"))
        print("With *")
        print(task4(arr, "*"))
        print("With ^")
        print(task4(arr, "^"))
        print("With XOR")
        print(task4(arr, "XOR"))



    def erfordnis5( arr:list[int]) -> None:
        print(task5(arr, formula="122//2-60+(x**(1+0)**2)=(12-11)*y-10+10"))

    def erfordnis6( arr:list[int]) -> None:
        print(task6(arr))

    def erfordnis7( arr:list[int]) -> None:
        print(task7(arr, start=0, stop=len(arr)-1))


if __name__ == "__main__":
    def main():
        arguments = input("Enter the array and then an option: ").split()
        arr = [int(elem) for elem in arguments[:len(arguments)-1]]
        option = int(arguments[len(arguments)-1])

        System = SysMeniu(arr, option)

        System.Exe()
        
    main()