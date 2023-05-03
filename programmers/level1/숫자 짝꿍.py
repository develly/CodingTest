from collections import Counter


def solution(X, Y):
    answer = ""
    x = Counter(X)
    y = Counter(Y)

    for i in range(9, -1, -1):
        answer += str(i) * min(x[str(i)], y[str(i)])

    if not answer:
        return "-1"

    if answer[0] == "0":
        return "0"

    return answer


if __name__ == '__main__':
    print(solution("100", "2345"))
