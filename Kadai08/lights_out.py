"""
工夫点
・簡易的なタイマーを設計
・難易度を選択できるようにする
・裏モードを追加（悪魔が時々盤面をランダムに全部崩す）
"""


import time,random

while True:
    try:
        level = int(input("難易度を選択してください : 1:簡単(3×3) 2:普通(5×5) 3:難しい(10×10) > "))
        print()

        if level == 1:
            size = 3
            break
        elif level == 2:
            size = 5
            break
        elif level == 3:
            size = 10
            break
        else:
            print("正しい難易度を選択してください\n")

    except ValueError:
        print("数字で入力してください\n")

while True:
    try:
        timerlevel = int(input("制限時間を決めてください : 1:簡単(無限)　2:普通(300)秒　3:(100)秒 > "))

        if timerlevel == 1:
            timer = None
            break
        elif timerlevel == 2:
            timer = 300
            break
        elif timerlevel == 3:
            timer = 100
            break
        else:
            print("正しい難易度を選択してください\n")

    except ValueError:
        print("数字で入力してください\n")

start_time = time.time()

devil = False

devil_mode = random.randint(1,5)

if devil_mode == 5:
    print("裏モード:devil\n悪魔が気まぐれに盤面を全て崩します")
    devil = True
    print("3秒後にゲームがスタートします")
    time.sleep(3)

board = [[0 for _ in range(size)] for _ in range(size)]

def isDevil(board):
    print("\n悪魔のいたずら")
    for b in range(len(board)):
        for a in range(len(board[b])):
            board[b][a] = random.randint(0,1)

def Cheange(board,x,y):
    position = [[x,y],[x+1,y],[x-1,y],[x,y+1],[x,y-1]]
    for a,b in position:
        if 0 <= a < size and 0 <= b < size:
            board[b][a] = 1 - board[b][a]

def Clear(board):
    for line in board:
        for dot in line:
            if dot == 0:
                return False
    return True

while True:    
    if timer is not None:
        elapsed = time.time() - start_time
        current_time = int(timer - elapsed)
        if current_time < 0:
            print("時間切れ！また遊んでね！")
            break
        
        print(f"\n残り時間:{current_time}秒",end="")
    else:
        print("\n制限時間:無限モード")

    print("現在のボード")
    for line in board:
        for dot in line:
            print(dot,end=" ")
        print()
    print()

    if Clear(board):
        print("\nゲームクリア！おめでとう！")
        break
    
    try:
        x = int(input(f"X座標を入力してください(1~{size})")) - 1
        y = int(input(f"Y座標を入力してください(1~{size})")) - 1
        print()
        if 0 <= x < size and 0 <= y < size:
            Cheange(board,x,y)
        else:
            print("正しい座標を入力してください\n")
            continue

    except ValueError:
        print("数字で入力してください\n")
        continue

    if devil:
        devil_change = random.randint(1,10)
        if devil_change == 1 or devil_change == 10:
            isDevil(board)
