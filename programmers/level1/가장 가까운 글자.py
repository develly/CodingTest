def solution(s):
    answer = []
    past = []
    for i, j in enumerate(s):
        if j not in past:
            answer.append(-1)
            past.append(j)
        else:
            answer.append(s[:i][::-1].find(j) + 1)

    return answer


if __name__ == '__main__':
    print(solution("banana"))
