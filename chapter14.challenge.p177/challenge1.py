class Square():
    square_list = []
    
    def __init__(self,side):
        self.side = side
        self.square_list.append(self)
        
squ1 = Square(4)
squ2 = Square(5)    

print(Square.square_list)

class Square2():
    square_list = []
    
    def __init__(self,side):
        self.side = side
        self.square_list.append(self)
    
    def __repr__(self):
        return "{} by {} by {} by {}".format(self.side,self.side,self.side,self.side)

squ3 = Square2(6)
squ4 = Square2(7)

print(Square2.square_list)

def IS_SQUARE(obj1, obj2):
    if obj1 is obj2:
        print("Both objects are the same square.")
    else:
        print("The objects are different squares.")

obj1 = input("Enter obj1 is:")
obj2 = input("Enter obj2 is:")
IS_SQUARE(eval(obj1), eval(obj2))
#eval() is used to convert the input string to the corresponding object.


