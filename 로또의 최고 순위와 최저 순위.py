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
