class trail :
    def __init__ (self,name,age) :
        self.name = name
        self.age  = age
    
    def methods(self) :
        print("Hi. My Name is " + self.name)
        print("My age is " + str(self.age))

a = trail("Niranjan", 17)

a.methods()



