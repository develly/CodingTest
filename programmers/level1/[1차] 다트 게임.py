import re


def solution(dartResult):
    dartResult = dartResult.replace('10', 'A')

    result = []
    for i in dartResult:
        if i == 'A':
            result.append(10)
        elif i.isdigit():
            result.append(int(i))
        elif i == 'S':
            pass
        elif i == 'D':
            result[-1] = result[-1] ** 2
        elif i == 'T':
            result[-1] = result[-1] ** 3
        elif i == '*' and len(result) >= 2:
            result[-1] = result[-1] * 2
            result[-2] = result[-2] * 2
        elif i == '*':
            result[-1] = result[-1] * 2
        elif i == '#':
            result[-1] = -result[-1]
        else:
            raise ValueError

    return sum(result)


def another_solution(dartResult):
    """Another solution to the same problem."""
    bonus = {'S': 1, 'D': 2, 'T': 3}
    option = {'': 1, '*': 2, '#': -1}

    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i - 1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    return sum(dart)


if __name__ == '__main__':
    print(solution('1S2D*3T'))
    print(another_solution('1D2S#10S'))
