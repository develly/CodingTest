def solution(strings, n):
    answer = []
    for i in strings:
        answer.append(i[n] + i)
    answer.sort()

    return list(map(lambda x: x[1:], answer))


def shortcut(strings, n):
    """Summarize the code in one line."""
    return sorted(strings, key=lambda x: x[n])


if __name__ == '__main__':
    print(solution(["sun", "bed", "car"], 1))
    print(shortcut(["sun", "bed", "car"], 1))
