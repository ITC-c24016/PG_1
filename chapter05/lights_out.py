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

board = [[0 for _ in range(size)] for _ in range(size)]

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
    except ValueError:
        print("数字で入力してください\n")
