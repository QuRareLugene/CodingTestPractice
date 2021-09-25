# 코딩테스트 연습 > Summer/Winter Coding(~2018) > 소수 만들기

# 주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다.
# 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때,
# nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때
# 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.

import math

def CheckPrime(Number):
    for i in range(2,int(math.sqrt(Number))+1):
        if Number%i==0:
            return False
    return True

def solution(nums):
    count = 0
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1, len(nums)):
                sum = nums[i] + nums[j] + nums[k]
                if CheckPrime(sum) == True:
                    count += 1
    return count