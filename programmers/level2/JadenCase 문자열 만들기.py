def solution(s):
    answer = ''
    for i in s:
        if i.isdigit():
            answer += i
        elif len(answer) == 0:
            answer += i.upper()
        elif len(answer) >= 1 and not answer[-1].isspace():
            answer += i.lower()
        elif len(answer) >= 1 and answer[-1].isspace():
            answer += i.upper()
        elif i.isspace():
            answer += " "

    return answer


if __name__ == '__main__':
    print(solution("3people unFollowed me"	))


