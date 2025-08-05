import random

randomNum = random.randint(1,10)
count = 0
while count < 10:
    ans = int(input("1~10の中の数字を入力してください"))

    if ans > randomNum:
        print("数字が大きいです")
        count += 1
        continue
    elif ans < randomNum:
        print("数字が小さいです")
        count += 1
        continue
    else:
        print("当たりです！")
        break

else:
    print("残念です")
