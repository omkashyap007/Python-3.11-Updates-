import asyncio

async def getNumber():
    return 1

async def getString():
    return "Hello World !"

async def getFloat():
    return 12.2342

async def groupTask():
    async with asyncio.TaskGroup() as tg : 
        number_task = tg.create_task(getNumber())
        string_task = tg.create_task(getString())
        float_task  = tg.create_task(getFloat())
    result = f"Result of getNumber = {string_task.result()}"
    return result

if __name__ == "__main__" : 
    print(asyncio.run(groupTask()))
    
# this is the use of context manager in asyncio , 
# lot of times , we forget to await the CoRoutines , its similar like opening a file and not closing it, 
# like  : file = open("file.txt" , "rb")
# so in order to manage the thing like  that, we use context managers , 
# similar to 
"""
with open("file.txt" , "rb") as f : 
    data = f.readlines()
"""
# with this new context manager for asyncio we do not need to await every CoRoutine , 
# just add to the task list . 