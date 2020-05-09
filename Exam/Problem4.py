class Cafe:
    menu = {"salad" : "10$" ,"pizza":"20$", "ice_cream":"5$" , "cake":"15$"}
    def __init__(self, name, tabels):
        self.name = name
        self.tabels = tabels
        
    def Reserve_table(self):
        if self.tabels > 0:
            self.tabels -= 1
            print("The reservation was made.")
        else:
            print("No available tables.")

    def Checkout(self, food):
        print("You have ordered", food , ".You have a", self.menu[food] ,"check" )
    
    
    
    def Order(self,food):
        if food in self.menu.keys():
            self.Checkout(food)
        else:
            print("We are out of food.")
    
    
    

sega = Cafe("Segafredo" , 2)
sega.Reserve_table()
sega.Checkout("pizza")
sega.Order("salad")

