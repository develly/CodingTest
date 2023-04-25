def solution(food):
    answer = ''
    for i in range(1, len(food)):
        num = food[i] // 2
        answer += str(i) * num

    return answer + '0' + answer[::-1]


if __name__ == '__main__':
    print(solution([1, 3, 4, 6]))
