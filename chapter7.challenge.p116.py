def challenge1():
    shows = ["ウォーキング・デッド", "アトランジュー", "ザ・ソプラノズ", "ヴァンパイア・ダイアリーズ"]
    for show in shows:
        print(show)

def challenge2():
    for i in range(25,51):
        print(i)

def challenge3():
    shows = ["ウォーキング・デッド", "アトランジュー", "ザ・ソプラノズ", "ヴァンパイア・ダイアリーズ"]
    #enumerate関数とは、リストの要素とそのインデックスを同時に取得するための関数です。
    for index, show in enumerate(shows):
        print(f"{index}: {show}")
    
def challenge4():
    passnumbers = [1234, 5678, 9012, 3456]
    #無限ループする数字あてゲームを作成する。qが入力されたら終了。数字が入力されたら正解かどうか判定
    while True:
        guess = input("パスワードを入力してください: ")
        if guess == "q":
            break
        try:
            guess = int(guess)
        except ValueError:
            print("数字を入力してください。")
            continue
        if guess in passnumbers:
            print("正解です！")
            break
        else:
            print("不正解です。もう一度試してください。")

def challenge5():
    #２つのリストに含まれるすべての数字の組み合わせで掛け算しよう
    list1 = [8,19,148,4]
    list2 = [9,1,33,83]
    added = []
    for num1 in list1:
        for num2 in list2:
            added.append(num1 * num2)
    print(added)

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
    
