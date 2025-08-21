"""
工夫点

・バッドエンド集(シークレット入り)を作り、条件分岐を増やしシークレットを出ずらくする
・ドラゴンをクラス化しドラゴンを一気に3体まで同時に飼えるようにする
・詰めすぎたら表示がごちゃごちゃになりやすい文章量だからちょうどいい具合のところで改行処理)
・行動回数をドラゴンの数×{i}回行動できるようにし、プレイヤーに難易度を選択できるようにする
・actionによって文字の色を変更
"""


import random,sys,time

#タイプライター(どうしてもやりたかったため少しAIを使用)
def slow_red(texts,delay=0.1,end=""):
    for text in texts:
        sys.stdout.write(f"\033[31m{text}\033[0m")
        sys.stdout.flush()
        time.sleep(delay)
        delay = max(0.004,delay * 0.8)
    print(end=end,flush=True)

#オリジナルバッドエンド集
def badEnd(name):
    line1 = "苦しい"
    line2 = "助けて"
    #条件を2段階に分けてシークレットエンドが出ずらいように設定
    number1 = random.randint(1,5)
    if number1 == 5:
        number2 = random.randint(1,5)
    else:
        number2 = random.randint(1,4)

    match number2:
        case 1:
            print(f"エンディング1 : \033[31mあなたは{name}に食べられてしまった...\033[0m")
        case 2:
            print(f"エンディング2 : \033[31mあなたは{name}に切り裂かれてしまった...\033[0m")
        case 3:
            print(f"エンディング3 : \033[31mあなたは{name}に潰されてしまった...\033[0m")
        case 4:
            print(f"エンディング4 : \033[31mあなたは{name}に焼き殺されてしまった...\033[0m")
        case 5:
            print(f"\033[35mシークレットエンド : {name}が怒ってあなたは永遠と{name}に飼われ同じ苦しみを味わうこととなった...\033[0m\n\n")

            time.sleep(5)
            slow_red(f"{line1}...\n",0.1)

            time.sleep(3)
            slow_red(f"{line1}...",0.1)

            time.sleep(0.5)
            slow_red(f"{line1}.....\n",0.1)

            time.sleep(4)
            slow_red(f"{line1 * 200}\n",0.15)

            time.sleep(0.05)
            slow_red(f"{line2 * 500}\n\n\n\n",0.07)

            time.sleep(7)
            print(".........いつしか声はでなくなっていた..........\n")

            time.sleep(3)
            print(".........意識が遠のく..........\n")
            
            time.sleep(3)
            print("...もうダメだ...\n")

            time.sleep(3)
            print("...過去には戻れない...\n")

            time.sleep(3)
            print("このまま一生飼われるのか...嫌だな...\n")

            time.sleep(3)
            print("...いっそ自分でﾀﾋのうかな...")

            time.sleep(2)
            change = input("自決しますか？(y/n) > ")

            if change == "y":
                print("\n\033[31mあなたは自決することを選んだ...\033[0m\n")

                time.sleep(3)
                print("\033[31mお父さん...お母さん...ごめんなさい.....\033[0m\n")

                time.sleep(3)
                print("END : ==「最後の逃亡 」==\n")
                time.sleep(1)
            else:
                print("\nそんな勇気は出なかった...\n")

                time.sleep(3)
                print(f"このまま永遠と{name}に飼われることとなった\n")

                time.sleep(3)
                print("END : == 「終わらない檻 」==\n")
                time.sleep(1)

#ドラゴンをクラス化(複数のドラゴンを飼えるようにするため)
class Dragon:
    def __init__(self,name):
        self.name = name
        self.hungry = 10 #満腹度
        self.satiety = 10 #機嫌度
        self.poop = 0 #ウンチ
        self.continuous_meal = 0 #連続でご飯を食べさせたかカウント
        self.cleaned_poop = False #ウンチを掃除したか？
        self.fed_today = False #ご飯を食べさせたか？
        self.sleep_today = False #寝かしつけたか？


    #ごはん
    def feed(self):
        #ご飯をあげようとしすぎたらストレスが溜まって殺される
        if self.continuous_meal >= 10:
            print(f"\n{self.name}がご飯を与えようとしすぎて怒ってしまった...\n")
            badEnd(self.name)
            sys.exit()

        #警告
        elif self.continuous_meal >= 7:
            print(f"\n{self.name}がストレスで殺意を剥き出しだ...\n")
            self.continuous_meal += 1
            return False

        elif self.hungry == 10:
            print(f"\n{self.name}は満腹で吐きそうだ...\n")
            self.continuous_meal += 1
            return False

        else:
            print(f"\n\033[33m{self.name}にご飯をあげた！\033[0m\n")
            self.hungry = min(10,self.hungry + 2)
            self.fed_today = True
            return True

    #掃除
    def clean(self):
        #ウンチを掃除してある場合
        if self.cleaned_poop:
            print(f"\n{self.name}のウンチはもうキレイにしてあるよ！\n")
            return False

        print(f"\n\033[36m{self.name}のウンチをキレイにした！\033[0m\n")
        self.hungry = max(0,self.hungry - 1)
        self.poop = 0
        self.cleaned_poop = True
        self.continuous_meal = 0
        return True

    #散歩
    def walk(self):
        print(f"\n\033[32m{self.name}と散歩に行った！\033[0m\n")
        self.hungry = max(0,self.hungry - 1)
        self.satiety = min(10,self.satiety + 1)
        self.continuous_meal = 0
        return True

    #睡眠
    def sleep(self):
        #選択したドラゴンが寝ている場合
        if self.sleep_today:
            print(f"\n{self.name}はもう寝ているよ！\n")
            return False

        print(f"\n\033[34m{self.name}を寝かしつけた！\033[0m\n")
        self.hungry = max(0,self.hungry - 2)
        self.satiety = min(10,self.satiety + 2)
        self.sleep_today = True
        self.continuous_meal = 0
        return True


    #一日の終わり
    def day_end(self):
        #ウンチを片付け忘れた場合
        if not self.cleaned_poop:
            satiety_loss = self.poop * 3
            self.satiety = max(0,self.satiety - satiety_loss)
            print(f"{self.name}のウンチを片付け忘れた！機嫌度が-{satiety_loss}された！")

        #ご飯をあげ忘れた場合
        if not self.fed_today:
            self.hungry = max(0,self.hungry - 3)
            print(f"{self.name}にご飯をあげ忘れた！満腹度が-3された！")

        #寝かしつけ忘れた場合
        if not self.sleep_today:
            self.satiety = max(0,self.satiety - 3)
            print(f"{self.name}に睡眠をあげ忘れた！機嫌度が-3された！")
        
        #リセット
        self.cleaned_poop = False
        self.fed_today = False
        self.sleep_today = False
        self.continuous_meal = 0


    #ゲームオーバー処理
    def is_dead(self):
        if self.hungry <= 0 or self.satiety <= 0:
            if self.hungry <= 0 and self.satiety <= 0:
                print(f"{self.name}がお腹をすかせまくり、機嫌を損ねまくって怒ってしまった...")
            elif self.hungry <= 0:
                print(f"{self.name}がお腹をすかせまくり怒ってしまった...")
            elif self.satiety <= 0:
                print(f"{self.name}が機嫌を損ねまくり怒ってしまった...")
            badEnd(self.name)
            return True
        return False


    #ステータス表示
    def status(self):
        poop_image = "💩" * self.poop
        print(f"{self.name}の状態 : 満腹度:{self.hungry} 機嫌度:{self.satiety} ウンチ:{poop_image}")


#メインゲーム処理
def main():
    print("\nドラゴンのお世話ゲーへようこそ！\n")
    while True:
        try:
            num = int(input("預かるドラゴンの数を決めてください(1~3) > "))
            print() #改行の為の空白print

            if 1 <= num <= 3:
                break
            else:
                print("\nerror : 1~3の数字で選択してください！\n")

        except ValueError:
            print("\nerror : 数字で入力してください！\n")

    
    while True:
        try:
            #行動回数を設定
            select = int(input(f"難易度を選択してください  1 (簡単:{num * 4}回行動)　2 (普通:{num * 3}回行動)　3 (難しい:{num * 2}回行動) > "))
            print() #改行の為の空白print
            
            if select == 1:
                level = num * 4
                break
            elif select == 2:
                level = num * 3
                break
            elif select == 3:
                level = num * 2
                break
            else:
                print("error : 1~3の数字で入力してください！")

        except ValueError:
            print("error : 数字で入力してください")

    dragons = [] #名前を付けたドラゴンを入れる箱

    for i in range(num):
        name = input(f"{i+1}匹目のドラゴンに名前を付けてあげましょう！ > ")
        dragons.append(Dragon(name))

    #名前表示
    print("\n名前決定！")
    for i,dragon in enumerate(dragons):
        print(f"{i+1}匹目:{dragon.name}")

    print("\nじゃあ早速お世話を始めよう！")

    days = 1 #日数

    while days <= 7:
        #ドラゴンの数だけ実行
        for dragon in dragons:
            dragon.poop += 1
            dragon.cleaned_poop = False
            dragon.fed_today = False
            dragon.sleep_today = False
            dragon.continuous_meal = 0

        command_count = 0 #コマンド入力
        last_action = None #最後に行った行動を記録
        last_target = -1 #最後のターゲットを記録

        print(f"\n{days}日目！{level}回行動できます！")

        while command_count < level:
            print(f"\n{command_count + 1}回目\n何をする？")
            try:
                action = int(input("1:食事 (満腹度+2)\n2:掃除 (満腹度-1、💩を0に)\n3:散歩 (満腹度-1、機嫌度+1)\n4:睡眠 (満腹度-2、機嫌度+2) > "))

            except ValueError:
                print("\nerror : 数字で入力してください！\n")
                continue

            #ドラゴン選択
            print("どのドラゴンにしますか？")
            for i,dragon in enumerate(dragons):
                print(f"{i+1}:{dragon.name}")
            
            try:
                target = int(input()) - 1

                if not (0 <= target < len(dragons)):
                    print("\n正しい番号で入力してください！")
                    continue
            except ValueError:
                print("\n数字で入力してください！")
                continue

            dragon = dragons[target]

            if action == 1:
                if not dragon.feed():
                    continue
            elif action == 2:
                if last_action == 2 and target == last_target:
                    print("\n連続で掃除はやりたくない\n")
                    continue
                if not dragon.clean():
                    continue
            elif action == 3:
                if last_action == 3 and target == last_target:
                    print("\n連続で散歩はやりたくない\n")
                    continue
                dragon.walk()
            elif action == 4:
                if not dragon.sleep():
                    continue
            else:
                print("\n1~4で入力してください\n")
                continue

            dragon.status()
            command_count += 1
            last_action = action
            last_target = target

        print(f"\n{days}日目のお世話が終わった！\n")

        for dragon in dragons:
            dragon.day_end()
            dragon.status()
            if dragon.is_dead():
                sys.exit()

        days += 1

    print("1週間預かり切った！\n")
    for dragon in dragons:
        print(f"{dragon.name}は元気に帰っていった！")

if __name__ == "__main__":
    main()
