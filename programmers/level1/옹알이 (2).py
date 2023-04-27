from itertools import groupby


def solution(babbling):
    answer = 0
    mapping = {"aya": 'A', "ye": 'B', "woo": 'C', "ma": 'D'}

    for i, j in enumerate(babbling):
        for k in mapping.keys():
            babbling[i] = babbling[i].replace(k, mapping[k])

        check_repeat = len([g for _, g in groupby(babbling[i]) if len(list(g)) > 1])
        if babbling[i].isupper() and not check_repeat:
            answer += 1
    return answer


def another_solution(babbling):
    """Another solution to the same problem."""
    count = 0
    for b in babbling:
        if "ayaaya" in b or "yeye" in b or "woowoo" in b or "mama" in b:
            continue
        if not b.replace("aya", " ").replace("ye", " ").replace("woo", " ").replace("ma", " ").replace(" ", ""):
            count += 1

    return count


if __name__ == '__main__':
    print(solution(["aya", "yee", "u", "maa"]))
    print(another_solution(["aya", "yee", "u", "maa"]))
