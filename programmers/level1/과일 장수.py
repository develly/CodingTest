def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    for i in range(len(score) // m):
        answer += min(score[i * m: i * m + m]) * m
    return answer


def shorten(k, m, score):
    """Summarize the code in one line."""
    return sum(sorted(score)[len(score) % m::m]) * m


if __name__ == '__main__':
    print(solution(3, 4, [1, 2, 3, 1, 2, 3, 1]))
    print(shorten(3, 4, [1, 2, 3, 1, 2, 3, 1]))
    print(shorten(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))
