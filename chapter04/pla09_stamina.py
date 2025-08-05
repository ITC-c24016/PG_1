import random , time

BOARD_SIZE = 30

event_tipe = {
    1: "金貨をゲット",
    2: "金貨をロス",
    3: "Xマス進む",
    4: "Xマス戻る",
    5: "1回休み",
    6: "振り出しに戻る"
}

stamina = {"player":6,"cpu":6}

def init_board():
    board = ["スタート"] + ["普通"] * (BOARD_SIZE - 2) + ["ゴール"]
    event_1to4_count = 10
    event_5_count = 3
    event_6_count = 1
    total_events = event_1to4_count + event_5_count + event_6_count
    event_positions = random.sample(range(1, BOARD_SIZE - 1), total_events)
    for pos in event_positions[:event_1to4_count]:
        event = random.randint(1, 4)
        x = random.randint(1, 3)
        board[pos] = f"{event_tipe[event]}({x})"
    
    for pos in event_positions[event_1to4_count:event_1to4_count + event_5_count]:
        board[pos] = event_tipe[5]

    for pos in event_positions[-event_6_count:]:
        board[pos] = event_tipe[6]

    return board


def move_player(current, dice, position, stamina):
    old_pos = position[current]
    next_pos = old_pos + dice

    if next_pos > BOARD_SIZE:
        over = next_pos - BOARD_SIZE
        next_pos = BOARD_SIZE - over
        print(f"出目が大きすぎ！{over}マス戻って {next_pos}マス目へ")
    elif next_pos == BOARD_SIZE:
        print(f"{current} がゴールにぴったり到達！")
        position[current] = next_pos
        return True
    else:
        print(f"{current} は {next_pos} マス目へ")

    moved = abs(next_pos - old_pos)
    stamina[current] = max(1, stamina[current] - moved)  # スタミナ減少

    position[current] = next_pos
    return False

def process_event(current, board, position, money, rest_turn,stamina):

    reached = False  # ゴール到達フラグ
    skip_display = False  # 移動イベントのあと追加出力をスキップするか

    pos = position[current]
    event = board[pos - 1]  # boardは0-indexなので-1

    print(f"{pos} マス目：{event}")

    # 各イベントの処理

    # 金貨をゲット(例: "金貨をゲット(3)")
    if event.startswith("金貨をゲット"):
        value = int(event.split("(")[1].strip(")"))
        money[current] += value
        print(f"💰 {value}枚ゲット！（合計 {money[current]}枚）")

    # 金貨をロス(例: "金貨をロス(2)")
    elif event.startswith("金貨をロス"):
        value = int(event.split("(")[1].strip(")"))
        money[current] = max(0, money[current] - value)
        print(f"💸 {value}枚ロス…（合計 {money[current]}枚）")

    # Xマス進む(例: "Xマス進む(2)")
    elif event.startswith("Xマス進む"):
        value = int(event.split("(")[1].strip(")"))
        new_pos = position[current] + value
        position[current] = new_pos
        print(f"➡ {value}マス進んで {new_pos}マス目へ！")
        skip_display = True  # 移動先イベントは発動しないので追加表示はスキップ
        return reached, skip_display

    # Xマス戻る(例: "Xマス戻る(1)")
    elif event.startswith("Xマス戻る"):
        value = int(event.split("(")[1].strip(")"))
        new_pos = max(1, position[current] - value)
        position[current] = new_pos
        print(f"⬅ {value}マス戻って {new_pos}マス目へ！")
        skip_display = True
        return reached, skip_display

    # 1回休み
    elif event == "1回休み":
        rest_turn[current] = rest_turn.get(current, 0) + 1
        stamina[current] = min(stamina[current] + 3,7)

        print("😴 1回休み！次のターンは休むよ")

    # 振り出しに戻る
    elif event == "振り出しに戻る":
        position[current] = 1
        print("🏠 振り出しに戻った！")

    # ゴール判定（boardにゴールがあれば）
    elif event == "ゴール":
        print("🎉 ゴール！")
        reached = True

    return reached, skip_display


def main():
    board = init_board()
    money = {"player": 10, "cpu": 10}
    position = {"player": 1, "cpu": 1}
    rest_turn = {"player": 0, "cpu": 0}
    reached_goal_flag = {"player": False, "cpu": False}
    players = ["player", "cpu"]
    turn = 0
    winner_speed = None

    print("🎲 すごろくゲームスタート！")
    print("ゴールにはピッタリ止まらないと到達できません！\n")

    while True:
        current = players[turn]

        # ゴールしてたらスキップ
        if reached_goal_flag[current]:
            print(f"{current} はすでにゴールしています。スキップ！")
            turn = (turn + 1) % 2
            continue

        if rest_turn[current] > 0:
            print(f"{current} は1回休み！")
            rest_turn[current] -= 1
            turn = (turn + 1) % 2
            continue

        if current == "player":
            button = input(f"{current} のターン！enter:サイコロを振る 1:食事を取る　(eで終了する) >> ")

            if button.lower() == "e":
                print("ゲームを終了します。")
                break

            if button == "1":
                if stamina[current] < 6 and money[current] >= 1:
                    money[current] -= 1
                    stamina[current] = 6
                    print(f"🍴 {current}は食事を取った！体力が6に回復！現在の金貨:{money[current]}")
                    continue
                else:
                    print("⚠ 金貨が足りないか、すでに体力が最大です")
                    continue
        else:
            print(f"{current}のターン！")
            if position["cpu"] < position["player"]:
                if stamina["cpu"] < 6 and money["cpu"] >= 1:
                    money["cpu"] -= 1
                    stamina["cpu"] = 6
                    print(f"🍴 {current}は食事を取った!体力が6に回復！現在の金貨:{money[current]}")
                    continue
                elif money["cpu"] < 1:
                    print(f"⚠ {current}は金貨がなく、食事できなかった！")
            else:
                print(f"{current}はまだリードしてるので食事しない")


        dice = random.randint(1, stamina[current])
        print(f"🎲 サイコロの目は {dice}！")

        reached = move_player(current, dice, position,stamina)
        reached_goal_flag[current] = reached
        #print(f"{current} のスタミナは {stamina[current]}")

        if reached:
            reached_goal_flag[current] = True
            if winner_speed is None:
                winner_speed = current
            print(f"📍 {current} の位置: {position[current]} / 💰 金貨: {money[current]}枚 / 💪 スタミナ: {stamina[current]}\n")
            if all(reached_goal_flag.values()):
                break
            time.sleep(1)
            turn = (turn + 1) % 2
            continue

        reached, skip_display = process_event(current, board, position, money, rest_turn, stamina)
        if reached:
            reached_goal_flag[current] = True
            if winner_speed is None:
                winner_speed = current

        print(f"📍 {current} の位置: {position[current]} / 💰 金貨: {money[current]}枚 / 💪 スタミナ: {stamina[current]}\n")

        if all(reached_goal_flag.values()):
            break
        if current == "player":
            time.sleep(1)
        else:
            time.sleep(0.5)
        turn = (turn + 1) % 2

    # ゲーム終了後：金銭的勝利
    if money["player"] > money["cpu"]:
        winner_money = "player"
    elif money["player"] < money["cpu"]:
        winner_money = "cpu"
    else:
        winner_money = "引き分け"

    if stamina["player"] > stamina["cpu"]:
        winner_stamina = "player"
    elif stamina["player"] < stamina["cpu"]:
        winner_stamina = "cpu"
    else:
        winner_stamina = "引き分け"

    print("🎉 ゲーム終了！")
    print(f"🏁 スピード的勝利: {winner_speed}")
    print(f"💰 金銭的勝利: {winner_money}")
    print(f"💪 スタミナ的勝利: {winner_stamina}")
    print(f"🧾 最終所持金 → player: {money['player']}枚 / cpu: {money['cpu']}枚")

if __name__ == "__main__":
    main()
