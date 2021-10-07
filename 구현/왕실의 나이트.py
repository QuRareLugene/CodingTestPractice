# Chapter 4. 구현 > 2. 왕실의 나이트
# 이것이 취업을 위한 코딩 테스트다 with 파이썬 (나동빈, 한빛미디어)

# 범위를 벗어났는지 확인한다. 벗어났으면 경우의 수를 1 차감한다.
def CheckOut(X,Y):
	if X<0 or X>7 or Y<0 or Y>7:
		return -1
	else:
		return 0

def solution(String):
	# X좌표를 알파벳에서 숫자로 변환하기 위한 dictionary
	XHint = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}

	# X좌표, Y좌표
	XLocation = XHint[String[0]]
	YLocation = int(String[1])-1
	#print("("+str(XLocation)+","+str(YLocation)+")")

	# 이동 가능한 총 경우의 수 8
	count = 8

	# 좌표를 하나씩 빼준다.
	count += CheckOut(XLocation+1, YLocation+2)
	#print("("+str(XLocation+1)+","+str(YLocation+2)+") = " + str(CheckOut(XLocation+1, YLocation+2)))
	#print(count)
	count += CheckOut(XLocation+1, YLocation-2)
	#print("("+str(XLocation+1)+","+str(YLocation-2)+") = " + str(CheckOut(XLocation+1, YLocation-2)))
	#print(count)
	count += CheckOut(XLocation+2, YLocation+1)
	#print("("+str(XLocation+2)+","+str(YLocation+1)+") = " + str(CheckOut(XLocation+2, YLocation+1)))
	#print(count)
	count += CheckOut(XLocation+2, YLocation-1)
	#print("("+str(XLocation+2)+","+str(YLocation-1)+") = " + str(CheckOut(XLocation+2, YLocation-1)))
	#print(count)
	count += CheckOut(XLocation-1, YLocation+2)
	#print("("+str(XLocation-1)+","+str(YLocation+2)+") = " + str(CheckOut(XLocation-1, YLocation+2)))
	#print(count)
	count += CheckOut(XLocation-1, YLocation-2)
	#print("("+str(XLocation-1)+","+str(YLocation-2)+") = " + str(CheckOut(XLocation-1, YLocation-2)))
	#print(count)
	count += CheckOut(XLocation-2, YLocation+1)
	#print("("+str(XLocation-2)+","+str(YLocation+1)+") = " + str(CheckOut(XLocation-2, YLocation+1)))
	#print(count)
	count += CheckOut(XLocation-2, YLocation-1)
	#print("("+str(XLocation-2)+","+str(YLocation-1)+") = " + str(CheckOut(XLocation-2, YLocation-1)))
	#print(count)

	return count

# 교재 모범답안
def solutionAlter(String):
	Row = int(String[1])
	Column = int(ord(String[0])) - int(ord('a')) + 1

	steps = [(-2,-1), (-1,-2), (1,-2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

	result = 0

	for step in steps:
		next_row = row + step[0]
		next_column = column + step[1]

		if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
			result += 1

	return result



Location = input()

print(solution(Location))