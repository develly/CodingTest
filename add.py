# 두개 뽑아서 더하기

def solution(numbers):
    answer = []
    for i in range(len(numbers)-1):
        for num in numbers[i+1:]:
            tmp = numbers[i] + num
            if tmp not in answer:
                answer.append(tmp)
    answer.sort()
    return answer

if __name__ == "__main__":
    numbers = [2,1,3,4,1]
    answer = solution(numbers)
    print(answer)
