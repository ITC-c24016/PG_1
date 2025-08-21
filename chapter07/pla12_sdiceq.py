import random

class Board:
    def __init__(self):
        self.panels = [str(i+1) for i in range(9)]
        self.opened = [False]*9
        self.traps = [0, 0]
        self.trap_on = False
        self.trap_block = False
        self.reset()

    def reset(self):
        self.panels = [str(i+1) for i in range(9)]
        self.opened = [False]*9
        nums = list(range(1, 10))
        random.shuffle(nums)
        self.traps = [nums[0], nums[1]]
        self.trap_on = False
        self.trap_block = False

    def all_open(self):
        return all(self.opened)

    def show(self):
        print("+ー+ー+ー+")
        for r in range(3):
            print("|", end="")
            for c in range(3):
                print(f"{self.panels[r*3+c]}|", end="")
            if r == 1:
                if self.trap_on:
                    print(" >>DON<< 警報！", end="")
                if self.trap_block:
                    print(" * DON 無効化 *", end="")
            print("\n+ー+ー+ー+")

    def open_panel(self, n):
        idx = n - 1
        if self.opened[idx]:
            print(f"パネル{n}はすでに開いてる")
            return False
        print(f"パネル{n}を開いた")
        self.panels[idx] = "Ｘ"
        self.opened[idx] = True
        return True

    def check_trap(self, n):
        idx = n - 1
        if n in self.traps:
            self.panels[idx] = "！"
            if self.trap_on:
                print(">> DON! << ゲームオーバー！")
                return True
            if self.trap_block:
                print("DON!は無効化されてる")
            else:
                print(">> DON! << 次もDONで終了！")
                self.trap_on = True
        else:
            if self.trap_on:
                print("DON!は無効化された")
                self.trap_block = True
            self.trap_on = False
        return False


class Game:
    def __init__(self):
        self.round = 1
        self.score = 0
        self.used = False
        self.remain = 0
        self.end = False
        self.dice = [0, 0]
        self.double = False

    def play(self, board):
        while True:
            print(f"\n*** Super Dice Q ***\nRound: {self.round}, Score={self.score}")
            self.dice = [random.randint(1, 6), random.randint(1, 6)]
            print(f"{self.dice[0]}と{self.dice[1]}が出た")
            self.used = False
            self.remain = sum(self.dice)
            self.double = (self.dice[0] == self.dice[1])
            if self.double:
                print("ゾロ目！ポイント2倍！")
            if self.no_panel(board):
                self.end = True
                break

            while True:
                board.show()
                print(f"残り: {self.remain}")
                choice = self.select()
                if choice == -1:
                    self.end = True
                    break
                if choice == 0:
                    if self.used:
                        print("振り直します")
                        break
                    print("開かないと振り直せない")
                    continue
                if board.open_panel(choice):
                    if board.check_trap(choice):
                        self.end = True
                        break
                    self.used = True
                    self.score += choice * (2 if self.double else 1)
                    self.remain -= choice
                    if board.all_open() and self.remain == 0:
                        print("全パネル開放！")
                        board.reset()
                        self.round += 1
                        break
                    if self.remain == 0:
                        print("残り0。振り直します")
                        break
                    if self.no_panel(board):
                        self.end = True
                        break
                else:
                    self.used = False
            if self.end:
                break

    def select(self):
        while True:
            try:
                n = int(input("どのパネル？(1-9, -1で終了) >> "))
                if n not in range(-1, 10) or n == 0:
                    print("1-9か-1を入力")
                    continue
            except ValueError:
                print("数字を入力")
                continue
            if n <= self.remain:
                return n
            print("残り目が足りない")

    def no_panel(self, board):
        max_check = min(self.remain, 9)
        if sum(board.opened[:max_check]) == max_check:
            board.show()
            print("開けるパネルなし。ゲームオーバー")
            return True
        return False


print("ゲーム開始")
b = Board()
g = Game()
while True:
    g.play(b)
    if g.end:
        break
print(f"結果: Round {g.round}, Score {g.score}")
print("終了")

