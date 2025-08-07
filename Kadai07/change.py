price = int(input())

money1_count = price // 100
price %= 100

money2_count = price // 10
price %= 10

money3_count = price

print(f"100円玉{money1_count}枚,10円玉{money2_count}枚,1円玉{money3_count}枚")


