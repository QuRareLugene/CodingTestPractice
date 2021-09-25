# 코딩테스트 연습 > 2021 Dev-Matching: 웹 백엔드 개발자(상반기) > 로또의 최고 순위와 최저 순위

# 로또 6/45(이하 '로또'로 표기)는 1부터 45까지의 숫자 중 6개를 찍어서 맞히는 대표적인 복권입니다.
# 아래는 로또의 순위를 정하는 방식입니다.

# 순위	당첨 내용
# 1	6개 번호가 모두 일치
# 2	5개 번호가 일치
# 3	4개 번호가 일치
# 4	3개 번호가 일치
# 5	2개 번호가 일치
# 6(낙첨)	그 외

# 로또를 구매한 민우는 당첨 번호 발표일을 학수고대하고 있었습니다.
# 하지만, 민우의 동생이 로또에 낙서를 하여, 일부 번호를 알아볼 수 없게 되었습니다.
# 당첨 번호 발표 후, 민우는 자신이 구매했던 로또로 당첨이 가능했던 최고 순위와 최저 순위를 알아보고 싶어 졌습니다.
# 알아볼 수 없는 번호를 0으로 표기하기로 하고, 민우가 구매한 로또 번호 6개가 44, 1, 0, 0, 31 25라고 가정해보겠습니다.
# 당첨 번호 6개가 31, 10, 45, 1, 6, 19라면, 당첨 가능한 최고 순위와 최저 순위의 한 예는 아래와 같습니다.

# 당첨 번호	31	10	45	1	6	19	결과
# 최고 순위 번호	31	0→10	44	1	0→6	25	4개 번호 일치, 3등
# 최저 순위 번호	31	0→11	44	1	0→7	25	2개 번호 일치, 5등

# 순서와 상관없이, 구매한 로또에 당첨 번호와 일치하는 번호가 있으면 맞힌 걸로 인정됩니다.

#민우가 구매한 로또 번호를 담은 배열 lottos, 당첨 번호를 담은 배열 win_nums가 매개변수로 주어집니다. 이때, 당첨 가능한 최고 순위와 최저 순위를 차례대로 배열에 담아서 return 하도록 solution 함수를 완성해주세요.

def solution(lottos, win_nums):
    HitCount = 0
    ZeroCount = 0
    
    for i in win_nums:
        if i in lottos:
            HitCount += 1
            
    for i in range (6):
        if lottos[i] == 0:
            ZeroCount += 1
    MaxResult = 6-HitCount-ZeroCount
    if MaxResult >=5:
        MaxNumber = 6
    else:
        MaxNumber = MaxResult + 1

    MinResult = 6-HitCount
    if MinResult >=5:
        MinNumber = 6
    else:
        MinNumber = MinResult + 1
        
    answer = [MaxNumber, MinNumber]
    return answer