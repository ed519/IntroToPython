from Productcheck import *

def buy(product,num,price):
    if check(product, num):
        print("Yout bought" , product , "and spent", num*price)
    else:
        print("Sorry! We are out of this product.")



def main():
    buy("candy" , 5, 10)





if __name__ == '__main__':
    main()    