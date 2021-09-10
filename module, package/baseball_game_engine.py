import random

#숫자야구게임
#퀴즈내자 숫자 3자리 중복없이
def make_quiz():

    list = random.sample(range(1, 10), 3)
    quiz = "".join(map(str, list))
    return quiz

def check (answer, player):
    strike = 0
    ball = 0
    for answer_num in answer:
        for player_num in player:
            if player_num in answer:
                if answer.index(answer_num) == player.index(player_num):
                    strike += 1
                else:
                    ball += 1

    #번호가 있고, 자리가 같으면 strike +=1
    #번호가 있고, 자리가 다르면 ball +=1
    return strike, ball


if __name__ == "__main__":
    answer = make_quiz()
    print(answer)
    strike, ball = check("238", "241")
    print(strike, ball)
    strike, ball = check("381","182")
    print(strike, ball)