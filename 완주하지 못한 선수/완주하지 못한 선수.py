# 코딩테스트 연습 > 해시 > 완주하지 못한 선수

# 수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

# 마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 
# 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

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