from itertools import combinations


def solution(nums):
    c = list(map(sum, combinations(nums, 3)))
    answer = len(c)
    for i in c:
        for j in range(2, i):
            if i % j == 0:
                answer -= 1
                break
    return answer


if __name__ == '__main__':
    print(solution([1, 2, 3, 4]))
