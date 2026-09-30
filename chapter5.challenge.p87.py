def challenge1_():
    musicains = ["Bach", "Beethoven", "Mozart", "Chopin", "Vivaldi"]
    print("音楽家のリスト:", musicains)
def challenge2_():
    my_taple = {"Tokyo": (35.6894, 139.6917), "New York": (40.7128, -74.0060), "London": (51.5074, -0.1278)}
    print("都市と座標:", my_taple)
def challenge3_():
    my_dict = {"身長": "170cm", "好きな柄":"曜変天目","好きな色":"花緑青","好きな作家":"恩田陸","好きな絵師":"井田千秋"}
    print("私の特徴:", my_dict)
def challenge4_():
    n = input("特徴を入力してください(身長, 好きな柄, 好きな色, 好きな作家, 好きな絵師): ")
    my_dict = {"身長": "170cm", "好きな柄":"曜変天目","好きな色":"花緑青","好きな作家":"恩田陸","好きな絵師":"井田千秋"}
    if n in my_dict:
        print(f"{n}は{my_dict[n]}です。")
"Pythonの組み込みコンテナの一つにsetがあります。setは、重複する要素を持たないコレクションです。"
"setは、リストやタプルのように順序を持たず、要素の追加や削除が可能です。"
"setは、数学的な集合の概念に基づいており、和集合、積集合、差集合などの演算が可能です。"
"setの作成は、波括弧{}を使用するか、set()関数を使用します。例えば、my_set = {1, 2, 3}やmy_set = set([1, 2, 3])のように作成できます。"
"setは、リストやタプルと同様にforループで反復処理が可能です。また、setは、要素の存在確認や重複排除などの操作に便利です。"
# すべての関数を順番に実行するコード
if __name__ == "__main__":
    print("--- チャレンジ1の実行 ---")
    challenge1_()

    print("\n--- チャレンジ2の実行 ---")
    challenge2_()

    print("\n--- チャレンジ3の実行 ---")
    challenge3_()

    print("\n--- チャレンジ4の実行 ---")
    challenge4_()
