#static method: a method which does not require the self attribute(object)
#class method:a method that uses class and not an abject as an argument
#property: it can use any method as a property(attribute)
class Student: 
    name="anonymous"
    @staticmethod
    def hello():
        print("Hello student")
    
    @classmethod
    def change_name(cls,name):
        cls.name=name #will change the name in the class itself
    
    def __init__(self,math,phy,chem):
        self.phy=phy
        self.math=math
        self.chem=chem
        
    @property
    def percentage(self):
        return (self.phy+self.math+self.chem)/3


    
    


s1=Student(97,98,99)
print(s1.percentage)
s1.phy=89
print(s1.percentage)
s1.change_name("rahul")
print(s1.name)
print(Student.name)
    


