def solution(n, m, section):
    answer = 1
    tmp = section[0] + m - 1
    for i in section[1:]:
        if i > tmp:
            answer += 1
            tmp = i + m - 1
    return answer


if __name__ == '__main__':
    print(solution(8, 4, [2, 3, 6]))
    # good test case
    print(solution(10, 3, [1, 5, 10]))
