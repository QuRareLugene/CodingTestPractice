# 코딩테스트 연습 > 월간 코드 챌린지 시즌2 > 음양 더하기
# https://programmers.co.kr/learn/courses/30/lessons/76501?language=python3

def solution(absolutes, signs):

    sum = 0
    print(signs)
    for i in range(len(absolutes)):
        if signs[i] == false:
            sum = sum - absolutes[i]
        else:
            sum = sum + absolutes[i]
    answer = sum
    return answer