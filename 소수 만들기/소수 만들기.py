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