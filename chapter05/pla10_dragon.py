import random,sys,time


#タイプライター
def slow_red(text, delay=0.1):
    for char in text:
        sys.stdout.write(f"\033[31m{char}\033[0m")
        sys.stdout.flush()
        time.sleep(delay)
        delay = max(0.004, delay * 0.8)
    print()


#バッドエンド集
def badEnd(name):
    lines1 = "苦しい"
    lines2 = "助けて"
    number = random.randint(1, 5)
    match number:
        case 1:
            print(f"エンディング1 : あなたは{name}に食べられてしまった...")
        case 2:
            print(f"エンディング2 : あなたは{name}に切り裂かれてしまった...")
        case 3:
            print(f"エンディング3 : あなたは{name}に潰されてしまった...")
        case 4:
            print(f"エンディング4 : あなたは{name}に焼き殺されてしまった...")
        case 5:
            print(f"エンディング5 : {name}が怒ってあなたは永遠と{name}に飼われ同じ苦しみを味わうこととなった...\n\n")

            time.sleep(5)
            slow_red(f"{lines1}...\n", 0.1)

            time.sleep(3)
            slow_red(f"{lines1}.....{lines1}.........\n", 0.1)

            time.sleep(4)
            slow_red(lines1 * 200 + "\n", 0.15)

            time.sleep(0.05)
            slow_red(lines2 * 500 + "................" + "\n\n\n\n", 0.07)

            time.sleep(7)
            print("..........いつしか声はでなくなって、意識が遠のいていく..........\n")

            time.sleep(3)
            print("もうダメだと悟った....\n")

            time.sleep(3)
            print("いつしかあなたの存在を覚えている人もいなくなっていた\n")

            time.sleep(3)
            print("もう戻れない。\n")

            time.sleep(3)
            print("END : ==「終わらない檻」==\n")
            time.sleep(1)



class Dragon:
    def __init__(self, name):
        self.name = name
        self.hungry = 10
        self.satiety = 10
        self.poop = 0
        self.continuous_meal = 0
        self.cleaned_poop = False
        self.fed_today = False
        self.slept_today = False

    #ごはん
    def feed(self):
        if self.continuous_meal >= 10:
            print(f"{self.name}がご飯を与えようとしすぎて怒ってしまった...\n")
            badEnd(self.name)
            sys.exit()

        if self.continuous_meal >= 7:
            print(f"{self.name}が殺意を剥き出しだ...\n早く別の行動をしないと\n")
            self.continuous_meal += 1
            return False

        if self.satiety >= 10:
            print(f"{self.name}は満腹で吐きそうだ\n")
            self.continuous_meal += 1
            return False

        print(f"{self.name}にご飯をあげた！")
        self.hungry = min(10, self.hungry + 2)
        self.poop += 1
        self.fed_today = True
        self.continuous_meal += 1
        return True

    #掃除
    def clean(self):
        if self.cleaned_poop:
            print(f"{self.name}のうんこはもうきれいにしてあるよ！\n")
            return False

        print(f"{self.name}のうんこを掃除した！")
        self.hungry = max(0, self.hungry - 1)
        self.poop = 0
        self.cleaned_poop = True
        self.continuous_meal = 0
        return True

    #散歩
    def walk(self):
        print(f"{self.name}と散歩に行った！")
        self.hungry = max(0, self.hungry - 1)
        self.satiety = min(10, self.satiety + 1)
        self.continuous_meal = 0
        return True

    #睡眠
    def sleep(self):
        if self.slept_today:
            print(f"{self.name}はもう寝ているよ！")
            return False

        print(f"{self.name}を寝かせた！")
        self.hungry = max(0, self.hungry - 2)
        self.satiety = min(10, self.satiety + 2)
        self.slept_today = True
        self.continuous_meal = 0
        return True

    #一日の終わり
    def day_end(self):
        if not self.cleaned_poop:
            satiety_loss = self.poop * 3
            self.satiety = max(0, self.satiety - satiety_loss)
            print(f"{self.name}のうんこを片づけ忘れた！機嫌度が-{satiety_loss}された！")

        if not self.fed_today:
            self.hungry = max(0, self.hungry - 3)
            print(f"{self.name}に食事を与えなかった！満腹度が-3された！")

        if not self.slept_today:
            self.satiety = max(0, self.satiety - 3)
            print(f"{self.name}に睡眠を与えなかった！機嫌度が-3された！")

        self.cleaned_poop = False
        self.fed_today = False
        self.slept_today = False
        self.continuous_meal = 0

    #バッドエンド
    def is_dead(self):
        if self.hungry <= 0 or self.satiety <= 0:
            if self.hungry <= 0 and self.satiety <= 0:
                print(f"{self.name}がお腹をすかせまくり機嫌を損ねまくって怒ってしまった")
            elif self.satiety <= 0:
                print(f"{self.name}の機嫌を損ねてしまい怒ってしまった")
            else:
                print(f"{self.name}がお腹をすかせすぎて怒ってしまった")
            badEnd(self.name)
            return True
        return False

    #ステータス表示
    def status(self):
        poop_emoji = "💩" * self.poop
        print(f"{self.name}の状態 → 満腹度: {self.hungry} 機嫌度: {self.satiety} うんこ: {poop_emoji}")



def main():
    print("ドラゴンのお世話ゲームへようこそ！")
    while True:
        try:
            num = int(input("預かるドラゴンの数を選んでください（1〜3） > "))
            if 1 <= num <= 3:
                break
            else:
                print("1〜3の数字を入力してください")
        except ValueError:
            print("数字で入力してください")

    dragons = []
    for i in range(num):
        name = input(f"{i+1}匹目のドラゴンの名前を決めてください > ")
        dragons.append(Dragon(name))

    print("\nじゃあ早速世話を始めよう！\n")

    days = 1
    while days <= 7:
        print(f"{days}日目\n")
        for doragon in dragons:
            doragon.poop += 1
            doragon.cleaned_poop = False
            doragon.fed_today = False
            doragon.slept_today = False
            doragon.continuous_meal = 0

        command_count = 0
        last_care = None
        last_target = -1

        max_actions = num * 4

        while command_count < max_actions:
            print("\n何をしますか？")
            print("1: 食事（満腹度+2）")
            print("2: 掃除（満腹度-1、💩を0に）")
            print("3: 散歩（満腹度-1、機嫌度+1）")
            print("4: 睡眠（満腹度-2、機嫌度+2）")

            try:
                care = int(input())
            except ValueError:
                print("数字で入力してください")
                continue

            print("どのドラゴンにしますか？")
            for i, doragon in enumerate(dragons):
                print(f"{i+1}: {doragon.name}")
            try:
                target = int(input()) - 1
                if not (0 <= target < len(dragons)):
                    print("正しい番号を入力してください")
                    continue
            except ValueError:
                print("数字で入力してください")
                continue

            doragon = dragons[target]

            if care == 1:
                if not doragon.feed():
                    continue
            elif care == 2:
                if last_care == 2 and target == last_target:
                    print("連続で掃除はやりたくない\n")
                    continue
                if not doragon.clean():
                    continue
            elif care == 3:
                if last_care == 3 and target == last_target:
                    print("連続で散歩は飽きちゃう\n")
                    continue
                doragon.walk()
            elif care == 4:
                if not doragon.sleep():
                    continue
            else:
                print("1〜4の数字を入力してください")
                continue

            doragon.status()
            command_count += 1
            last_care = care
            last_target = target

            if doragon.is_dead():
                sys.exit()

        print(f"\n{days}日目の世話が終わった!\n")

        for doragon in dragons:
            doragon.day_end()
            doragon.status()
            if doragon.is_dead():
                sys.exit()

        days += 1

    print(f"1週間預かり切った!")
    for doragon in dragons:
        print(f"{doragon.name}は元気に帰っていった！")

if __name__ == "__main__":
    main()
