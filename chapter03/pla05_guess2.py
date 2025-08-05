import random

def game():
    randomNum = random.randint(1,10)
    count = 0
    life = 5
    ansNum = 5

    while ansNum > 0 and count < 5:
        try:
            ans = int(input("1~10の中の数字を入力してください"))

            if ans == 0:
                print("ゲームを終了します")
                break

            if ans > randomNum:
                print("数字が大きいです")
                life -= 1
                count += 1
                print(f"現在の点数は{life}です！")
                continue
            elif ans < randomNum:
                print("数字が小さいです")
                life -= 1
                count += 1
                print(f"現在の点数は{life}です！")
                continue
            else:
                print("当たりです！")
                life += 10
                ansNum -= 1
                count = 0
                print(f"現在の点数は{life}です！")
                randomNum = random.randint(1,10)

        except ValueError:
            print("数字で入力してください")
            continue

    print(f"最終的な点数は{life}です！")

while True:
    game()

    retry = input("もう一度やりますか？(y/n)").lower()
    if retry != "y":
        print("終了します")
        break
