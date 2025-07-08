constellation = ["水瓶座", "魚座", "牡羊座", "牡牛座", "双子座", "蟹座",
                 "獅子座", "乙女座", "天秤座", "蠍座", "射手座", "山羊座"]

switch_days = [20, 19, 21, 20, 21, 22, 23, 23, 23, 24, 23, 22]
max_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def Seiza():
    while True:
        print("生まれた月を入力してください")
        try:
            month = int(input())
            if 1 <= month <= 12:
                break
            else:
                print()
                print("error : 正しい月を入力してください")
                print()
        except ValueError:
            print()
            print("error : 正しい月を入力してください")
            print()

    while True:
        print()
        print("生まれた日を入力してください")
        try:
            day = int(input())
            if 1 <= day <= max_days[month - 1]:
                break
            else:
                print()
                print("error : 正しい日付を入力してください")
        except ValueError:
            print()
            print("error : 正しい日付を入力してください")

    if day < switch_days[month - 1]:
        index = 11 if month == 1 else month - 2
    else:
        index = month - 1

    answer = constellation[index]
    print()
    print(f"入力された値 : {month}月{day}日")
    print(f"あなたの星座は{answer}です")

while True:
    Seiza()
    print()
    retry = input("もう一回やりますか？(y/n)").lower()
    if retry != "y":
        print("終了します")
        break
