def solution(n):
    answer = 0
    for i in range(2, n + 1):
        flag = 0
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                flag = 1
                break
        if not flag:
            answer += 1

    return answer


def another_solution(n):
    """Using the Sieve of Eratosthenes.
    """
    num = set(range(2, n + 1))

    for i in range(2, n + 1):
        if i in num:
            num -= set(range(2 * i, n + 1, i))
    return len(num)


if __name__ == '__main__':
    print(solution(10))
    print(another_solution(10))
