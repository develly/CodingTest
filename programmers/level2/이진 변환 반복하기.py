def solution(s):
    answer = [0, 0]

    while True:
        # del 0
        t = s.replace("0", "")

        # add num of 0
        nums = len(s) - len(t)
        answer[1] += nums
        answer[0] += 1

        # update s
        s = format(len(t), 'b')

        # check break point
        if s == "1":
            break

    return answer


def another_solution(s):
    """Another solution to the same problem."""
    a, b = 0, 0

    # break point
    while s != '1':
        # update a
        a += 1
        # count 1 !!
        num = s.count('1')
        # update b
        b += len(s) - num
        # bin
        s = format(num, 'b')

    return [a, b]


if __name__ == '__main__':
    print(solution("110010101001"))
    print(another_solution("110010101001"))
