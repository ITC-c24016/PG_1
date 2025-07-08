def intChack(number):
    while True:
        user_input = input(number)
        if user_input.isdigit():
            return user_input
        else:
            print("数字で入力してください")

def Suhi():
    print("生まれた年を入力してください")
    year = intChack("")

    print("生まれた月を入力してください")
    month = intChack("")

    print("生まれた日を入力してください")
    day = intChack("")

    dateOfBirth = year + month + day

    total = 0
    for i in dateOfBirth:
        total += int(i)

    strFateNumber = str(total)

    fateNumber = 0
    for l in strFateNumber:
        fateNumber += int(l)

    print(f"あなたの運命数は{fateNumber}です！")

while True:
    Suhi()
    print()
    retry = input("もう一回やりますか(y/n)").lower()
    if retry != "y":
        print("終了します")
        break
