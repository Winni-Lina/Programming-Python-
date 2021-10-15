from baseball_game_engine import make_quiz, check
from custom_error import InvalidCountError
answer = make_quiz()

#무한 반복
count = 0


def save_history(player, count):
    with open("baseball_history.txt", 'a') as f:
        f.write(f'{player}\t{count}\n')


def load_history():
    count_list = []
    with open('baseball_history.txt','r') as f:
        while True:
            line=f.readline()
            if line == '':
                break
            # print(line.rstrip())
            line_data = line.rstrip().split('\t')
            print(line_data[1])
            count_list.append(line_data[1])
        count_list = set(count_list)
        count_list = list(count_list)
        count_list.sort()
        print(count_list[:3])

while True:
# 숫자 3자리 중복없이 묻자
    player = input("숫자 세자리는?(t: top3)")
    if player == "t":
        history = load_history()
        print(history)
        continue

    try:
        player_int = int(player)
    except ValueError:
        continue
    if len(player) != 3:
        #raise InvalidCountError("3자리가 아닙니다.")
        print(f'입력한 숫자의 개수가 정답과 다릅니다. 정답: {len(answer)} 글자')
        continue

# strike, ball 확인하자
    count += 1
    strike, ball = check(answer, player)
# 출력하자
    print(f"{player}\tstrike: {strike}\tball: {ball}\t{count} try")
# strike가 3일 때, 나가자
    if strike == 3:
        # 저장하자
        save_history(player, count)
        break

#축하해주자
print("축하합니다!")