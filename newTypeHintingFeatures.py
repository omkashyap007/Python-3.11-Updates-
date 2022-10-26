from typing import TypeVar
from typing import Generic
from typing import TypeVarTuple
from typing import LiteralString
from typing import NewType
from typing import List
from typing import Self

# normal data types  type hinting .
a : int = 10 
b : str = "string"
c : list[int] = [1 , 2 ,3 ]
d : tuple[str] = ("a" , "b" , "c")
e : dict[str , int] = {"number" : 10 }

# This functoin takes list of numbers and then returns a string .  as defined in function type hints
def oddEven(list_of_numbers : List[int]) -> str : 
    ans = sum(list_of_numbers)
    return ["Even" , "Odd"][ans%2]

print(oddEven([1,2,3]))

DType = TypeVar("Dtype") # defines a Datatype 
Shape = TypeVarTuple("Shape")
# TypeVarTuple helps to annotate fininte but unspecified type of objects . 
# like :  list ( a : int , b : str , c : dict)
# *Shape
# TypeVarTuple is still under devlopment so much information cannot be provided .


# creating new data types for our own simplicity and usage . 
# the Height , Length , Width will remain int but Length will also of data type of int . 
Length = NewType("Length" , int)
Width = NewType("Width" , int)
Height = NewType("Height" , int)

class NewDataType(Generic[DType , *Shape]):
    ... 

# this creates a new data type class with Generic data type , the first argument tells about other
# data types which are in the list . 


# literal string

def literal_string(string : LiteralString):
    a = string[::-1]
    b = f"This is literal string { string }"
    c = " ".join(a , b)
    
    # these all will remain literal strings .
    
# literal strings will give a gentle reminder that there is a literal string in the code . 
