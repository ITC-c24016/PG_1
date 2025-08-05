import random

count = 0

playerWin = 0
cpuWin = 0

hand = ["グー","チョキ","パー"]
win = {"グー":"チョキ","チョキ":"パー","パー":"グー"}

def game():
    playerWin = 0
    cpuWin = 0
    count = 0
    
    while count < 10:
        cpuHand = random.choice(hand)

        try:
            playerHand = int(input("1:グー、2:チョキ、3:パーの中から数字で選んでください"))
        except ValueError:
            print("error : 数字で入力してください(1~3)")
            continue

        if playerHand == 1:
            player = hand[0]
        elif playerHand == 2:
            player = hand[1]
        elif playerHand == 3:
            player = hand[2]
        else:
            print("error : 1:グー、2：チョキ、3:パーの中から選んでください")
            continue

        print(f"あなたの手:{player} 相手の手:{cpuHand}")

        if player == cpuHand:
            print("あいこ！もう一回！")
            continue
        elif win[player] == cpuHand:
            playerWin += 1
            count += 1
            print(f"{count}回目、あなたの勝利！")
            continue
        else:
            cpuWin += 1
            count += 1
            print(f"{count}回目、あなたの負け...")
            continue

    if playerWin > cpuWin:
        print(f"あなたの勝利回数:{playerWin}回　相手の勝利回数:{cpuWin}回")
        print("あなたの勝利！おめでとう！")
    elif playerWin < cpuWin:
        print(f"あなたの勝利回数:{playerWin}回　相手の勝利回数:{cpuWin}回")
        print("残念、あなたの負け...")
    else:
        print(f"あなたの勝利回数:{playerWin}回　相手の勝利回数:{cpuWin}回")
        print("引き分け！")

while True:
    game()

    retry = input("もう一度プレイしますか？(y/n)").lower()
    if retry != "y":
        print("ゲームを終了します")
        break
