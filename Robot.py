from Weapon import Weapon


class Robot:
    def __init__ (self):
        self.name = ""
        self.health: int
        self.weapon: Weapon()
    
    def set_name(self):
        self.name = input("Please enter a robot name: ")
        print ("Robot name:", self.name)
    


    
   