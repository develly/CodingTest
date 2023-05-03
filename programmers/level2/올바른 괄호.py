def solution(s):
    if s[0] == ")":
        return False

    stack = []
    for i in s:
        stack.append(i)

        if len(stack) >= 2 and ''.join(stack[-2:]) == '()':
            stack.pop(-1)
            stack.pop(-1)

    return True if not stack else False


if __name__ == '__main__':
    print(solution("()()"))
