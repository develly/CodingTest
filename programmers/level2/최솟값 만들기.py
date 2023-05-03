def solution(A, B):
    answer = 0
    B.sort(reverse=True)
    for i, j in enumerate(sorted(A)):
        answer += j * B[i]
    return answer


def shorten(A, B):
    """Summarize the code in one line."""
    return sum([a * b for a, b in zip(sorted(A), sorted(B, reverse=True))])


if __name__ == '__main__':
    print(solution([1, 4, 2], [5, 4, 4]))
    print(shorten([1, 4, 2], [5, 4, 4]))
