products = {"candy" : 10 , "juice": 5 , "pen":50}

def check(product , num):
    if products.get(product)  and products.get(product) >= num:
        return True
    else:
        return False
        