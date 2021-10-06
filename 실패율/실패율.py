# 코딩 테스트 연습 > 2019 KAKAO BLIND RECRUITMENT > 실패율

# https://programmers.co.kr/learn/courses/30/lessons/42889?language=python3

def solution(N, stages):
    Survivor = len(stages)
    Result = []
    Answer = []
    for i in range(1, N+1):
        Survivor = Survivor - stages.count(i-1)
        if Survivor !=0:
            Failrate = float(stages.count(i))/float(Survivor)
        else:
            Failrate = 0.0
        Result.append((i, Failrate))
    Result.sort(key=lambda x:x[1], reverse=True)
    for i in range(len(Result)):
        Answer.append(Result[i][0])
    return Answer