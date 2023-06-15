def solution(n, words):
    stack = []
    for i in range(len(words)):
        if len(stack) == 0:
            stack.append(words[i])
            continue

        if (stack[-1][-1] != words[i][0]) or words[i] in stack:
            q, r = divmod(i + 1, n)
            if r == 0:
                return [n, q]
            else:
                return [r, q + 1]

        stack.append(words[i])

    return [0, 0]


def another_solution(n, words):
    """Another solution to the same problem."""
    for p in range(1, len(words)):
        if words[p][0] != words[p - 1][-1] or words[p] in words[:p]:
            return [(p % n) + 1, (p // n) + 1]
    else:
        return [0, 0]


if __name__ == '__main__':
    print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
