from itertools import combinations


def solution(number):
    return sum([1 if sum(i) == 0 else 0 for i in combinations(number, 3)])


if __name__ == '__main__':
    print(solution([-2, 3, 0, 2, -5]))
