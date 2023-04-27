def solution(number, limit, power):
    answer = 0
    for i in range(1, number + 1):
        cnt = 0
        for j in range(1, int(i ** 0.5) + 1):
            if i % j == 0 and j ** 2 != i:
                cnt += 2
            elif i % j == 0:
                cnt += 1

        if cnt <= limit:
            answer += cnt
        else:
            answer += power

    return answer


if __name__ == '__main__':
    print(solution(5, 3, 2))
