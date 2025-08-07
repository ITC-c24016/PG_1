import random

suits = ["ハート","ダイヤ","スペード","クローバー"]
ranks = ["A"] + [str(i) for i in range(2,11)] + ["J","Q","K"]
card = [(suit,rank) for suit in suits for rank in ranks]

random.shuffle(card)

print("あなたが引いたトランプは、")

for i in range(5):
    suit,rank = card[i]
    print(f"{suit}の{rank}")

print("です。")
