# Chapter 3. 그리디 > 3. 숫자 카드 게임
# 이것이 취업을 위한 코딩 테스트다 with 파이썬 (나동빈, 한빛미디어)

def solution(BaYeol, YSize, XSize):
	# Mins = 각 줄의 최소값
	Mins = 0
	# CurrentMin = 최소값중 최대값
	CurrentMin = 0
	# 한 줄씩 탐색한다.
	for i in range(int(YSize)):
		Matrix = BaYeol[i].split(' ')
		# 각 줄마다 최소값을 찾는다.
		for j in range(int(XSize)):
			Value = Matrix[j]
			if j == 0:
				Mins = Value
			elif Value < Mins:
				Mins = Value
		# 줄마다 최소값의 최대값을 찾는다.
		if i == 0:
			CurrentMin = Mins
		elif Mins > CurrentMin:
			CurrentMin = Mins

	return CurrentMin

# 교재 모범답안
def solutionAlter():
	n, m = map(int, input().split())

	result = 0

	for i in range(n):
		data = list(map(int, input().split()))
		min_value = 10001
		for a in data:
			min_value = min(min_value, a)
	result = max(result, min_value)

# 확인용 main
#SizeOfMatrix = input().split(' ')

#QuestionMatrix = []
#for i in range(int(SizeOfMatrix[0])):
#	QuestionMatrix.append(input())

#print(solution(QuestionMatrix, SizeOfMatrix[0], SizeOfMatrix[1]))