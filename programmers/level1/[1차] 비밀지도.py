def solution(n, arr1, arr2):
    answers = []
    for i, j in zip(arr1, arr2):
        i_bin = format(i, 'b').zfill(n)
        j_bin = format(j, 'b').zfill(n)

        answer = ""
        for k in range(n):
            if any([int(i_bin[k]), int(j_bin[k])]):
                answer += '#'
            else:
                answer += ' '
        answers.append(answer)
    return answers


def another_solution(n, arr1, arr2):
    """Another solution to the same problem."""
    answer = []
    for i, j in zip(arr1, arr2):
        a12 = str(bin(i | j)[2:])
        a12 = a12.rjust(n, '0')
        a12 = a12.replace('1', '#')
        a12 = a12.replace('0', ' ')
        answer.append(a12)
    return answer


if __name__ == '__main__':
    n = 5
    arr1 = [9, 20, 28, 18, 11]
    arr2 = [30, 1, 21, 17, 28]
    print(solution(n, arr1, arr2))
    print(another_solution(n, arr1, arr2))
