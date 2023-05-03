def solution(s):
    s = list(map(int, s.split()))
    return f"{min(s)} {max(s)}"


if __name__ == '__main__':
    print(solution("1 2 3 4"))

