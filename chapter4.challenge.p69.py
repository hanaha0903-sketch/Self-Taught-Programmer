def challenge1(x):
    return x**2

def challenge2(x):
    return str(x)

def challenge3(x,y,z,w=1,v=2):
    return x + y + z + w + v

def challenge4():
    x = input("type a number: ")
    x = int(x)
    def amari(x):
        return x % 2
    result = amari(x)
    def kakezan(result):
        return result * 4
    return kakezan(result)

def challenge5():
    x= input("type a sentence:")
    try:
        x = float(x)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return None
    return x

# （上の関数定義の続きとして、一番下に貼り付け）

if __name__ == "__main__":
    print("--- challenge1 のテスト (引数: 4) ---")
    print("結果:", challenge1(4)) 
    print()

    print("--- challenge2 のテスト (引数: 100) ---")
    print("結果:", repr(challenge2(100))) # 文字列になっているか分かりやすく表示
    print()

    print("--- challenge3 のテスト (引数: 10, 20, 30) ---")
    print("結果:", challenge3(10, 20, 30))
    print()

    print("--- challenge4 のテスト (入力が必要) ---")
    print("結果:", challenge4())
    print()

    print("--- challenge5 のテスト (入力が必要) ---")
    print("結果:", challenge5())

