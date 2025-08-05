e = int(input("英語の成績を入力してください"))
m = int(input("数学の成績を入力してください"))
score = ""

if e >= 90 and m >= 90:
    score = "S"
elif 70 <= e < 90 or 70 <= m < 90:
    score = "A"
elif 50 <= e < 70 or 50 <= m < 70:
    score = "B"
elif e < 50 and m < 50:
    score = "C"

print(f"あなたの成績は{score}です！")
