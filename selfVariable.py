from typing import Self

class TestingClass:
    def __init__(self , a :int ) -> Self : 
        self.a = a

    @classmethod
    def obj_from_string(cls : Self , string : str) :
        return cls(int(string))
a = TestingClass(10)
b = TestingClass.obj_from_string("23")
print(b)

# Earlier version of python would use Optional["TestingClass"] type hint for representing the 
# self object .