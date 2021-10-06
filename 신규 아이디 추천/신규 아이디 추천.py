# 코딩테스트 연습 > 2021 KAKAO BLIND RECRUITMENT > 신규 아이디 추천
# https://programmers.co.kr/learn/courses/30/lessons/72410?language=python3

def solution(new_id):
    # 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
    new_id = list(new_id.lower())
    Temporary = list(new_id)
    DeleteCount = 0
    
    # 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
    for i in range(len(new_id)):
        #print(str(i) + "/" + str(len(new_id)))
        #print(ord(new_id[i]))
        if (ord(new_id[i]) < 45 or
            ord(new_id[i]) > 57 or
            ord(new_id[i]) == 47):
            #print("Check 1")
            #print(Temporary)
            if (ord(new_id[i]) < 95 or
                ord(new_id[i]) > 122 or
                ord(new_id[i]) == 96):
                #print("Check 2")
                Temporary.remove(new_id[i])
                #print(Temporary)
            
    #print(Temporary)
    new_id = Temporary
    #print(new_id)
    
    # 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
    Temporary = ''.join(new_id)

    while (".." in Temporary):
        Temporary = Temporary.replace("..", ".")
    Temporary = list(Temporary)
    # 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    if Temporary[0]==".":
        del Temporary[0]
    elif Temporary[-1]==".":
        del Temporary[-1]
        
    # 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
    if len(Temporary) == 0:
        Temporary.append("a")

    # 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    if len(Temporary) > 15:
        Temporary = Temporary[0:15]
        
    # 6-1단계 만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
    if Temporary[-1]==".":
        del Temporary[-1]
        
    # 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    if len(Temporary) <= 2:
        while(len(Temporary)<3):
            Temporary.append(Temporary[-1])

    Result = ''.join(Temporary)
    #print(Result)
    return Result