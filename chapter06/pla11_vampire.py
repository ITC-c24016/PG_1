import random,sys

class Player:
    def __init__(self):
        self.explored_surface = [False]*6
        self.explored_underground = [False]*6
        self.has_key = False
        self.has_map = False
        self.has_cross = False
        self.location = '地上'  # '地上' or '地下'
        self.sanity = 8
        self.treasure = 0
        self.time = 14  # 14時スタート

    def sanity_check(self):
        fear = random.randint(1,10)
        if fear > self.sanity:
            self.sanity -= 1
            print()
            print(f"恐ろしいものを見てしまった！ 正気度が1減った。現在の正気度：{self.sanity}")
            print()
            if self.sanity <= 0:
                print("正気を失った君はもう、探索はできなくなった。ゲームオーバー。")
                sys.exit()

    def advance_time(self):
        self.time += 1
        if self.time >= 24:
            print()
            print("24時になり、吸血鬼が目覚め襲いかかってきた！")
            print()
            return True
        return False

    def update_after_explore(self, item, mansion):
        print()
        if item == 'はずれ':
            points = random.randint(1,3)
            self.treasure += points
            print(f"財宝を{points}ポイント見つけました！ 現在の財宝：{self.treasure}ポイント")
        elif item == '鍵':
            self.has_key = True
            print("カギを手に入れた！")
        elif item == '地図':
            self.has_map = True
            print("地図を手に入れた！")
        elif item == '地下入口':
            # 地下入口はここでは処理しない
            pass
        elif item == '十字架':
            self.has_cross = True
            print("十字架を見つけた！ 戦闘で有利になるぞ。")
        elif item == '吸血鬼':
            print("吸血鬼がいた！！")
            self.sanity -= 1
            print(f"恐怖で正気度が1減った。現在の正気度：{self.sanity}")
            mansion.battle(self)
        print()

class Mansion:
    def __init__(self, player):
        self.player = player
        self.surface_items = ['鍵','地図','地下入口'] + ['はずれ']*3
        self.underground_items = ['十字架','吸血鬼'] + ['はずれ']*4
        random.shuffle(self.surface_items)
        random.shuffle(self.underground_items)
        self.surface_explored = [False]*6
        self.underground_explored = [False]*6

    def display_map(self):
        print()
        print("††† 吸血鬼の館 †††")
        print(f" 1 2 3 4 5 6 \t時刻：{self.player.time}時")
        print("+-+-+-+-+-+-+")
        row = "|"
        for i,item in enumerate(self.surface_items):
            # 地下入口は鍵なしで見つけた時は探索済みにならない
            if self.surface_explored[i] or self.player.has_map:
                row += self.symbol(item) + "|"
            else:
                row += " |"
        print(row)
        print("+-+-+-+-+-+-+")
        if self.player.location == '地下' or self.player.has_map:
            row = "|"
            for i,item in enumerate(self.underground_items):
                if self.underground_explored[i] or self.player.has_map:
                    row += self.symbol(item) + "|"
                else:
                    row += " |"
            print(row)
            print("+-+-+-+-+-+-+")
        print(f"現在位置：{self.player.location}")
        print("カギ=k, 地図=m, 地下入口=d, 十字架=x, 吸血鬼=v")
        print(f"正気度：{self.player.sanity} / 財宝：{self.player.treasure}ポイント")
        print()

    def symbol(self, item):
        return {
            '鍵':'k', '地図':'m', '地下入口':'d',
            '十字架':'x', '吸血鬼':'v', 'はずれ':'0'
        }.get(item, ' ')

    def explore_area(self, idx):
        if self.player.location == '地上':
            item = self.surface_items[idx]

            # 鍵なしで地下入口を探索した場合は探索済みにしないでメッセージだけ
            if item == '地下入口' and not self.player.has_key:
                print()
                print(f"{idx+1}番のエリアを探索します。")
                print()
                self.player.advance_time()
                print("地下の入り口を見つけたけど、鍵がないので入れない。")
                print()
                return True

            # 鍵ありで地下入口探索した場合は探索済みにして地下に潜る
            if item == '地下入口' and self.player.has_key:
                if not self.surface_explored[idx]:
                    self.surface_explored[idx] = True
                    print()
                    print(f"{idx+1}番のエリアを探索します。")
                    print()
                    time_up = self.player.advance_time()
                    print("地下の入り口を見つけた！ 鍵があるから地下に入れる。")
                    print()
                    self.player.location = '地下'
                    if time_up:
                        self.battle(self.player)
                    return True
                else:
                    print()
                    print("もう探索済みの場所です。")
                    print()
                    return False

            # 通常の地上エリア処理
            if self.surface_explored[idx]:
                print()
                print("もう探索済みの場所です。")
                print()
                return False
            self.surface_explored[idx] = True
            time_up = self.player.advance_time()
            print()
            print(f"{idx+1}番のエリアを探索します。")
            print()
            self.player.update_after_explore(item, self)
            if time_up:
                self.battle(self.player)
            if self.player.sanity <= 0:
                sys.exit()
            if item != '吸血鬼':
                self.player.sanity_check()
            return True

        else:  # 地下探索
            if self.underground_explored[idx]:
                print()
                print("もう探索済みの場所です。")
                print()
                return False
            self.underground_explored[idx] = True
            item = self.underground_items[idx]
            time_up = self.player.advance_time()
            print()
            print(f"{idx+1}番のエリアを探索します。")
            print()
            self.player.update_after_explore(item, self)
            if time_up:
                self.battle(self.player)
            if self.player.sanity <= 0:
                sys.exit()
            if item != '吸血鬼':
                self.player.sanity_check()
            return True

    def battle(self, player):
        print()
        print("吸血鬼との戦闘！サイコロを振ります！")
        print()
        p_roll = random.randint(1,6)
        if player.has_cross:
            print("十字架の加護で+3！")
            p_roll += 3
        if player.treasure >= 10:
            print("財宝の重さで-2！")
            p_roll -= 2
        v_roll = random.randint(1,6)

        print(f"あなたの出目：{p_roll}")
        print(f"吸血鬼の出目：{v_roll}")
        print()

        if p_roll > v_roll:
            print("おめでとう！ 吸血鬼を倒すことができた！")
            print(f"あなたは財宝{player.treasure}ポイントを持ち帰った。")
        elif p_roll < v_roll:
            print("残念！ 吸血鬼にやられてしまった…")
        else:
            print("そこには静寂があった。")
            print("立ち上がる者はなく、")
            print("ただひんやりとした空気だけがただよっていた。")
            print("あなたが吸血鬼を倒したのは事実だ。")
            print("だが、それを誰にも報告することはできない。")
            print("しばしの時を経て、誰かがあなたの偉業に気付く。")
            print("その時には、すでに吸血鬼の館はなく、")
            print("白い花が一輪咲いていた…")
        sys.exit()

def main():
    player = Player()
    mansion = Mansion(player)

    while True:
        mansion.display_map()
        try:
            choice = int(input("どのエリアを探索しますか？(1-6): "))
            if 1 <= choice <= 6:
                mansion.explore_area(choice-1)
            else:
                print()
                print("1から6の数字を入力してください。")
                print()
        except ValueError:
            print()
            print("数字を入力してください。")
            print()

if __name__ == "__main__":
    main()
