import tomllib

# you can not parse tomllib files , you always have to read them as read binary . 
# currently i do not have a tomllib file , but download from net or somewhere , you'll get it. 
# we till now do not ability to write toml files , we can atleast read them . 
def fetchFile():
    with open("tomllib_file.py" , "rb") as f :
        data = tomllib.load(f)
    
    print(data)
    
if __name__ == "__main__" :  
    fetchFile()