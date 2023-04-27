import numpy as np


def solution(N, stages):
    """This solution throws a timeout error.
    Presumably np.where() is slow.
    """
    result = {}
    for i in range(1, N + 1):
        num = sum(np.where(np.array(stages) >= i, True, False))
        ratio = stages.count(i) / num
        result[i] = ratio

    return sorted(result, key=result.get, reverse=True)


def efficient_solution(N, stages):
    result = {}
    people = len(stages)
    for i in range(1, N + 1):
        if people:
            ratio = stages.count(i) / people
            people -= stages.count(i)
            result[i] = ratio
        else:
            result[i] = 0

    return sorted(result, key=result.get, reverse=True)


if __name__ == '__main__':
    print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
    print(efficient_solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
