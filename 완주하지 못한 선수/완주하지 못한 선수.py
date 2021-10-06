# 코딩테스트 연습 > 해시 > 완주하지 못한 선수
# https://programmers.co.kr/learn/courses/30/lessons/42576?language=python3

def solution(a, b):
    lists = a
    count = {}
    for i in lists:
        try: count[i] += 1
        except: count[i]=1
    for i in b:
        count[i] -= 1
            
    bb = {v:k for k,v in count.items()}
    T = list(bb)            
    return bb.get(max(T))