def solution(k, score):
    award = []
    answer = []
    for i, j in enumerate(score):
        if i < k:
            award.append(j)
            answer.append(min(award))
            continue
        if min(award) < j:
            award.remove(min(award))
            award.append(j)
        answer.append(min(award))

    return answer


def another_solution(k, score):
    """Another solution to the same problem."""
    award = []
    answer = []
    for s in score:
        award.append(s)
        if len(award) > k:
            award.remove(min(award))
        answer.append(min(award))

    return answer


if __name__ == '__main__':
    print(solution(3, [10, 100, 20, 150, 1, 100, 200]))
    print(another_solution(3, [10, 100, 20, 150, 1, 100, 200]))
