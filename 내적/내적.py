# 코딩테스트 연습 > 월간 코드 챌린지 시즌 1 > 내적
# https://programmers.co.kr/learn/courses/30/lessons/70128?language=python3

def solution(a, b):
    sum = 0
    
    for i in range(len(a)):
        sum += a[i]*b[i]

    answer = sum
    return answer