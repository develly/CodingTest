def solution(s):
    stack = []
    for i in s:
        if len(stack) == 0:
            stack.append(i)
            continue

        if stack[-1] == i:
            stack.pop()

        else:
            stack.append(i)

    return 0 if stack else 1


if __name__ == "__main__":
    print(solution('baabaa'))
