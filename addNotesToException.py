def findDivideResult(a , b):
    return a/b
def function_one():
    try : 
        answer = findDivideResult(10, 0)
    except ZeroDivisionError as e : 
        # adding notes to the error messages .
        e.add_note("Probably you are dividing the number by zero !")
        raise
        answer = None
    return answer
# adding notes to the exceptions , will genetly help what may have happen and giving a note is quite
# good update  .     
    

if __name__ == "__main__" : 
    function_one()
    