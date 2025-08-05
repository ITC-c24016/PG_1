import random

hand = ["グー", "チョキ", "パー"]
win = {"グー": "チョキ", "チョキ": "パー", "パー": "グー"}
finger_cost = {"グー": 0, "チョキ": 2, "パー": 5}

def game():
    playerWin = 0
    cpuWin = 0
    count = 0
    player_fingers = 18
    cpu_fingers = 18

    while count < 10:
        cpu_possible = [h for h in hand if finger_cost[h] <= cpu_fingers]
        if not cpu_possible:
            print("CPUの指が足りなくなりました。あなたの勝ちです！")
            break

        cpuHand = random.choice(cpu_possible)

        try:
            playerHand = int(input(f"1:グ- , 2:チョキ, 3:パー の中から数字で選んでください:(残り指の数{player_fingers}) "))
        except ValueError:
            print("数字を入力してください")
            continue

        if playerHand not in [1, 2, 3]:
            print("1～3の数字を入力してください")
            continue

        player = hand[playerHand - 1]
        cost = finger_cost[player]

        if player_fingers < cost:
            print(f"指が足りません。{player}は{cost}本の指を使います。残りは{player_fingers}本です。")
            continue

        print(f"あなた:{player}　相手:{cpuHand}")

        player_fingers -= cost
        cpu_fingers -= finger_cost[cpuHand]

        count += 1  # 勝負回数としてカウント（あいこ含む）

        if player == cpuHand:
            print(f"{count}回目、あいこ！")
            continue
        elif win[player] == cpuHand:
            if count == 6 or count == 10:
                playerWin += 2
            else:
                playerWin += 1
            print(f"{count}回目、あなたの勝利！")
        else:
            if count == 6 or count == 10:
                cpuWin += 2
            else:
                cpuWin += 1
            print(f"{count}回目、あなたの負け...")

    # 勝利回数から残り指分を引く
    playerWin -= player_fingers
    cpuWin -= cpu_fingers
    playerWin = max(playerWin, 0)
    cpuWin = max(cpuWin, 0)

    print("\n最終結果")
    print(f"あなたの点数:{playerWin}点　相手の点数:{cpuWin}点")
    if playerWin > cpuWin:
        print("あなたの勝利！おめでとう！")
    elif playerWin < cpuWin:
        print("残念、あなたの負け...")
    else:
        print("引き分け！")

while True:
    game()
    retry = input("\nもう一度プレイしますか？(y/n): ").lower()
    if retry != "y":
        print("ゲームを終了します")
        break

