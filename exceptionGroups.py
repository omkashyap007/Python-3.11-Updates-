import asyncio

async def findNumber():
    raise TypeError

async def findString():
    raise ValueError

async def findDict():
    raise ConnectionError

async def findList():
    raise IndexError

async def createGroupException():
    result = await asyncio.gather(
        findNumber() , 
        findString() , 
        findDict() , 
        findList() , 
        return_exceptions = True , 
    )
    exceptions = [ exc for exc in result if isinstance(exc , Exception)]
    if exceptions : 
        raise ExceptionGroup("There are few excpetions : " , exceptions)
    
async def main() :
    await createGroupException()
    
if __name__ == "__main__" :
    asyncio.run(main())
    
"""
The errors are raised on every CoRoutine ( function ) which is called , but using ExceptionGroup , 
we can group them and show in a ladder format for all the exceptions raised . 

"""