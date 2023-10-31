# # To find any pair (x,y) where x and y satisfy a arithmetical formula
# # We need to break the formula down and analyse each operator(each of them is placed on the sides of the = sign)
# # We will create a function execute(num1, num2) that supplies us with the mathematical computation based on the 
# # operation(+, *, /, %, //, **, |, &, ^)
# # And in the main body for whenever we find a var in the formula and we don't have yet an operation at disposal
# # We will move the value of the variable in a rez (which will be refered as our accumulation register)
# # When a operand is encountered in the formula and we have an operation then we can Execute the operation 


class Operation:
    
    def __init__(self, sign="", exists=False):
        self.sign= sign
        self.exists = exists


def Execute(operand1: int, operand2: int, operation: str)-> int:
    rez = 0
    match operation:
        case "+":
            rez = operand1 + operand2
        case "-":
            rez = operand1 - operand2
        case "*":
            rez = operand1 * operand2
        case "/":
            rez = operand1 / operand2
        case "%":
            rez = operand1 % operand2
        case "//":
            rez = operand1 // operand2
        case "**":
            rez = operand1 ** operand2
        case "|":
            rez = operand1 | operand2
        case "&":
            rez = operand1 & operand2
        case "^":
            rez = operand1 ^ operand2
        case _:
            raise TypeError("Operation invalide, a sing has been passed that doesn't match ant known operation")
    return rez
    

_possible_operations = ["+", "-", "*", "/", "**", "//", "|", "^", "&"]
_acummulators: list[int] = [0]
_operations: list[Operation] = [Operation()]

def Cleaning():
    _acummulators[0] = 0
    _operations[0].exists = False
    _operations[0].sign = ""


def Compute(*, formula: str, start: int, stop: int, x, y ) -> None:
    current_depth = 0
    placeholder_number = ""

    print(_operations[current_depth])
    for index in range(start, stop):
        char = formula[index]

        # In case the character is a operation sign we count that operation as the current valid one with which we compute the result
        # The current operation is the relation between the operand1 and operand2 used in Execute() function 
        # The Special case - which must be treated here - is when ** or // appears which in definitely is just a concatenation of 2 / or *
        # And to make the difference between only assigning / and concatenating // we compare the current char with the previous one
        if char in _possible_operations:
            if char == _operations[current_depth].sign :
                _operations[current_depth].sign += char
            else :
                _operations[current_depth].sign = char
                _operations[current_depth].exists = True
        
        # Case where there's a bracket and a new subenvironment of calculation must be initialise
        # we add a new Accumulator and a related Operation for its bracket calculation
        elif char == "(":
            _acummulators.append(0)
            _operations.append(Operation())
            current_depth += 1

        # When returning to a higher calculation environment we must first: save the value computed insinde the brackets
        # second: delete all the memory used for computation inside the bracket 
        # third: computing the new value in the higher calculation environment if there is an operation already available or
        # if not just to assing the value to the higher Accumulator
        elif char == ")":
            prev_accumulator = _acummulators[current_depth]
            del _acummulators[current_depth]
            del _operations[current_depth]
            current_depth -= 1
            if _operations[current_depth].exists :
                _acummulators[current_depth] = Execute(_acummulators[current_depth], prev_accumulator, _operations[current_depth].sign)
            else :
                _acummulators[current_depth] = prev_accumulator
        
        #if not all the above cases, than we have an operand encountered so we must treat all the possible cases in which either
        # 1. a variable (x, y) has been encountered, or 2. a number of 1, or more digits has been encountered
        else :
            # if there is a digit in the current char and it is a part of already encountered number with many digits
            # Then we glue the digits together
            if char != "x" and char != "y":
                if placeholder_number == "":
                    placeholder_number = char
                else :
                    placeholder_number += char
            else :
                #Very important is to treat the case of an existing operation available where we compute mathematically a result
                # and the case in which we just mov a value to the current Acummulator
                if _operations[current_depth].exists :
                    current_value = _acummulators[current_depth]
                    if char == "x":
                        _acummulators[current_depth] = Execute(current_value, x, _operations[current_depth].sign)
                    elif char == "y":
                        _acummulators[current_depth] = Execute(current_value, y, _operations[current_depth].sign)
                else :
                    if char == "x":
                        _acummulators[current_depth] = x
                    elif char == "y":
                        _acummulators[current_depth] = y

        # The last big case in our formula is when we release the placeholder_number( a number of 1 to many digits)
        # in this case we use the value in computation when the next character is not a digit(also by taking care of the current available operation)
        if index+1 >= len(formula) or formula[index+1] in _possible_operations  or formula[index+1] == "=" or formula[index+1] == ")" :
            if placeholder_number != "" and _operations[current_depth].exists :
                _acummulators[current_depth] = Execute(_acummulators[current_depth], int(placeholder_number), _operations[current_depth].sign)

            elif placeholder_number != "" and _operations[current_depth].exists == False:
                _acummulators[current_depth] = int(placeholder_number)

            placeholder_number = "" 

        print(placeholder_number)
        print(_acummulators)

def VerifyTheFormula(x: int, y: int, *, formula: str) -> bool:
    left_term: int
    right_term: int
    equal_idx = formula.index("=")

    #Compute the left term on the left side of equal
    Compute(formula=formula, x=x, y=y, start=0, stop=equal_idx)
        
    #Save the first term and reset the _accumulator and _operations on the top level(global) for the second term calculation
    left_term = _acummulators[0]
    Cleaning()
    
    Compute(formula=formula, x=x, y=y, start=equal_idx+1, stop=len(formula))
    
    #Save the last term and we go for comparing them in order to determine the relation truth value
    #and clean the global vars for the next cycle
    right_term = _acummulators[0]
    Cleaning()
    
    return left_term == right_term
    

def erofrod5(arr: list[int], *, formula: str) -> list[tuple]: 
    rez: list[tuple] = []

    for idx1 in range(len(arr)-1):
        for idx2 in range(idx1 + 1, len(arr)):
            if VerifyTheFormula(arr[idx1], arr[idx2], formula=formula) or VerifyTheFormula(arr[idx2], arr[idx1], formula=formula):
                rez.append((arr[idx1], arr[idx2]))
    return rez
    


# erofrod5([3, 8, 12, 34, 2, 22], formula="x**2+((y-(x+2))//3)=10")
