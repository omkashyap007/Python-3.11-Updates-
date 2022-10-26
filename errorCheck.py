def returnItem():
    return {
        "user_id" : 3242 , 
        "type" : "testing_checkout" , 
        "data" : {
            "order_id" : 876 ,  
            "payment_mode" : "paytm" , 
            "is_paid" : True , 
            "material_dispatched" : False , 
            "price" : 610 , 
            "quantity" : 5 ,
            "list_data" : [1 , 2 , 3]
        }
    }

def getPrice():
    data = returnItem()
    return data["data"]["price"] * data["data"]

if __name__ == "__main__" :
    price = getPrice()
    print(price)
"""
The function getPrice wil give error because i am trying to multiple integer with a dictionary object
Earlier python versions used to give only traceback and the line in which error occured . 

But now it will tell exactly where the error occured , it will make a pointer to the character 
or place where the error has occured .

example : 
return data["data"]["price"] * data["data"]
-----------------------------^-------------


"""