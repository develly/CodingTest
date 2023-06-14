def solution(n):
    answer = n
    num = format(n, 'b').count('1')

    while True:
        answer += 1
        if num == format(answer, 'b').count('1'):
            break

    return answer


if __name__ == "__main__":
    print(solution(15))
