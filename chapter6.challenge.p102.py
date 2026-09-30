# -*- coding: shift_jis -*-
def challenge1():
    kamyu="カミュ"
    print(kamyu[0])
    print(kamyu[1])
    print(kamyu[2]) 

def challenge2():
    print("文字列を２つ入力してください：")
    str1 = input()
    str2 = input()
    print(f"あなたが入力した文字列は「{str1}」と「{str2}」です。")
    #先頭のfはフォーマット文字列を意味します。{}内に変数を入れることで、文字列の中に変数の値を埋め込むことができます。
    str3 = f"私は昨日「{str1}」と「{str2}」を食べました。"
    print(str3)

def challenge3():
    str = "aldoux Huxley was born in 1894.".capitalize()
    print(str)

def challenge4():
    str = "どこで？誰が？何を？いつ？なぜ？どのように？"
    print(str.split("？"))
    
def challenge5():
    word = ["The", "fox", "jumped", "over", "the", "fence", "."]
    print(" ".join(word))
    #最後のピリオドの前に空白はいらないため、最後の要素を取り除いたリストを作成し、join()メソッドで結合します。
    print(" ".join(word[:-1]) + word[-1])
    """
    word[:-1]の意味は、リストwordの最初の要素から最後の要素の1つ前までをスライスして新しいリストを作成することです。
    つまり、最後の要素を除いたリストを作成します。
    """
    
def challenge6():
    str = "screaming comes across the sky"
    print(str.replace("s", "$"))
    
def challenge7():
    str = "Hemingway"
    print(str.index("m"))

def challenge8():
    """
    クォート文字とは文字列を囲むために使用される記号のことです。
    Pythonでは、シングルクォート（'）またはダブルクォート（"）を使用して文字列を定義できます。
    文字列内でクォート文字を使用する場合、エスケープシーケンスを使用してクォート文字を表現することができます。
    例えば、文字列内でシングルクォートを使用したい場合は、バックスラッシュ（\）を使用してエスケープすることができます。
    例：''Hello, it\'s a beautiful day!'
    エスケープシーケンスとは、特定の文字を表現するために使用される特殊な文字列のことです。
    エスケープシーケンスは、バックスラッシュ（\）で始まり、特定の文字を表現するために使用されます。終わりはありません。
    """
    str = "'Hello, it\'s a beautiful day!'"
    print(str)

def challenge9():
    str1 = "three"
    str2 = "three"
    str3 = "three"
    print(str1 + str2 + str3)
    print(str1 * 3)
    
def challenge10():
    str = "４月の晴れた寒い日で、時計がどれも十三時を打っていた。"
    print(str[0:10])
    
if __name__ == "__main__":
    print("--- チャレンジ1の実行 ---")
    challenge1()

    print("\n--- チャレンジ2の実行 ---")
    challenge2()

    print("\n--- チャレンジ3の実行 ---")
    challenge3()

    print("\n--- チャレンジ4の実行 ---")
    challenge4()
    
    print("\n--- チャレンジ5の実行 ---")
    challenge5()   
    
    print("\n--- チャレンジ6の実行 ---")
    challenge6()    
    
    print("\n--- チャレンジ7の実行 ---")
    challenge7()    
    
    print("\n--- チャレンジ8の実行 ---")
    challenge8()    
    
    print("\n--- チャレンジ9の実行 ---")
    challenge9()    
    
    print("\n--- チャレンジ10の実行 ---")
    challenge10()
    
