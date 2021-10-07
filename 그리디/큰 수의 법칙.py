# Chapter 3. 그리디 > 2. 큰 수의 법칙
# 이것이 취업을 위한 코딩 테스트다 with 파이썬 (나동빈, 한빛미디어)

def solution(InString, Numbers):
	# N, M, K가 공백으로 구분되어 입력
	Input = InString.split(' ')
	Numbers = Numbers.split(' ')
	# 배열의 크기 N
	N = int(Input[0])
	# 숫자가 더해지는 총 횟수 M
	M = int(Input[1])
	# 같은 숫자가 최대 더해질 수 있는 횟수 K
	K = int(Input[2])

	# 최대와 두번째 최대를 지정
	Max = 0
	SecondMax = 0

	for i in range(N):
		# Max보다 크고 SecondMax보다 크다면
		if (int(Numbers[i]) > Max) and (int(Numbers[i]) > SecondMax):
			# 현 Max 값이 SecondMax값이 되고 Numbers[i] 값은 Max 값이 된다.
			SecondMax = Max
			Max = int(Numbers[i])
		# Max보다 작지만 SecondMax보다 크다면
		elif (int(Numbers[i]) < Max) and (int(Numbers[i]) > SecondMax):
			# Numbers[i] 값은 SecondMax값이 된다.
			SecondMax = int(Numbers[i])
	# (최대 더할 수 있는 횟수 + 한번)의 배열이 총 길이에 몇번 들어가는지를 본다.
	Mok = M//(K+1)
	# 나머지는 무조건 Max들이다.
	Rem = M%(K+1)
	
	# (최대 더할 수 있는 횟수*Max + 1*SecondMax 를 몫 만큼 곱한 다음 나머지 Max를 더한다.
	Answer = (Mok*((Max*K)+SecondMax)) + (Rem*Max)
	return Answer 

# 확인용 main
#A = input()
#B = input()

#print(solution(A, B))