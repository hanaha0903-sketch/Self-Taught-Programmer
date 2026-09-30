class Shape:
    def what_am_I(self):
        return "I am a shape"
        
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

    # ★修正1: インデントを戻し、第一引数に `self` を追加しました
    def change_size(self, num):    
        # ★修正2: Squareは self.width と self.height を使うので、両方を更新します
        self.width = self.width + num  
        self.height = self.height + num

class Horse:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner

class Rider:
    def __init__(self, name):
        self.name = name

# --- 実行部分 ---

# challenge1    
Rec1 = Rectangle(5, 10)
Squ1 = Square(4)

shapes = [Rec1, Squ1]

for shape in shapes:
    print(f"Perimeter: {shape.calculate_perimeter()}")

# challenge2
# ★修正3: input()で受け取った文字列を int() で数値に変換します
num = int(input("Squareの辺の長をいくら変えますか?: "))

Squ1.change_size(num)

print(f"perimeter:{Squ1.calculate_perimeter()}")

# challenge3
# ★修正4: メソッドを呼び出すために後ろにカッコ `()` を付けました
print(Rec1.what_am_I(), Squ1.what_am_I())

# challenge4
Olivia = Rider("Olivia Valledstorm")
Pele = Horse("Pele", Olivia)

# ★修正5: Pele.Olivia.name ではなく Pele.owner.name に直しました
print(f"{Pele.name} の騎手は{Pele.owner.name}だ。")




    



