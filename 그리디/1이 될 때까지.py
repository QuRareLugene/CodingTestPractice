# Chapter 3. 그리디 > 4. 1이 될 때까지
# 이것이 취업을 위한 코딩 테스트다 with 파이썬 (나동빈, 한빛미디어)

def solution(N, K):
	N = int(N)
	K = int(K)
	count = 0

	# N이 1이 아닌 동안
	while(N!=1):
		# N을 K로 나눈 나머지가 0이라면
		if N%K==0:
			# N을 K로 나눈 몫이 새 N이 되고 count를 증가시킨다.
			N = N//K
			count +=1
		# N을 K로 나눈 나머지가 0이 아니라면
		else:
			# N에서 1을 빼고 count를 증가시킨다.
			N = N-1
			count +=1
		if N==1:
			break
	return count

# 교재 모범답안
def solutionAlter():
	n, k = map(int, input().split())
	result = 0

	while True:
		# (N==K로 나누어떨어지는 수)가 될 때까지 1씩 빼기
		target = (n//k)*k
		result += (n-target)
		n = target
		# N이 K보다 작을 때 반복문 탈출
		if n<k:
			break
		result += 1
		# K로 나누기
		n //=k

	# 마지막으로 남은 수에 대해 1씩 빼기
	result += (n-1)
	return result


Numbers = input().split(' ')

print(solution(Numbers[0], Numbers[1]))