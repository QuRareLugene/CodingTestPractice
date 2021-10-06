# 코딩테스트 연습 > 2019 카카오 개발자 겨울 인턴십 > 크레인 인형뽑기 게임
# https://programmers.co.kr/learn/courses/30/lessons/64061?language=python3

def solution(board, moves):
    # Count는 파괴된 인형의 숫자.
    Count = 0
    # Garbage는 뽑은 인형의 리스트
    Garbage = []
    # board[0]부터 [len(board)]까지 [moves[i]]번째를 확인
    for i in range(len(moves)):
        for j in range(len(board)):
            # 0일 경우 넘어가고 0이 아니라면
            if board[j][moves[i]-1] != 0:
                # Garbage에 append한다.
                Garbage.append(board[j][moves[i]-1])
                # Garbage의 길이가 2 이상일 경우
                if len(Garbage) > 1:
                    # 방금 집어넣은것과 맨 위에 있던 인형이 같은 인형이면
                    if Garbage[-1] == Garbage[-2]:
                        # 두 인형을 없애고 Count를 2 증가시킨다.
                        Garbage.pop()
                        Garbage.pop()
                        Count += 2
                # 값 다 넣었으면 그 인형은 board에서 삭제.
                board[j][moves[i]-1] = 0
                # j값은 더 증가시키지 않고 탈출한다.
                break
    return Count