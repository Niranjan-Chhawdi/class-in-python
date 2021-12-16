class dictionary :
    def __init__ (self, name , klass , add) :
        self.name  = name
        self.klass = klass
        self.add   = add
    
    def display (self) :
        print("Name    : " , self.name)
        print("Class   : " , self.klass)
        print("Address : " , self.add)

mat = input("In which format you want to add records \n 1.List \n 2.Tuple \n 3.Dictionary \n type 1 , 2 , 3 : ")

if mat == "1" :
    n = input("Enter the name    : ")
    c = input("Enter the class   : ")
    a = input("Enter the Address : ")

    





# b = dictionary(n , c , a)


# b.display()







