class Student:
    def __init__(self,name,phy,chem,math):
        self.name=name
        self.physics=phy
        self.chemistry=chem
        self.math=math
    
    def average(self):
        avg=(self.physics+self.chemistry+self.math)/3
        return avg

#creating an object
s1=Student("charvee",96,92,89)
print("Average",s1.average())
