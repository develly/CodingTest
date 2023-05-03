import numpy as np


def solution(board, moves):
    answer = 0
    bucket = []
    board = np.array(board)

    for i in moves:
        col = i - 1
        nonzero = np.nonzero(board[:, col])[0]
        if len(nonzero):
            row = nonzero[0]
        else:
            continue
        toy = board[row, col]

        if toy != 0:
            bucket.append(toy)
            board[row, col] = 0

        if len(bucket) > 1 and bucket[-1] == bucket[-2]:
            answer += 2
            bucket = bucket[:-2]

    return answer


def another_solution(board, moves):
    """Another solution to the same problem."""
    answer = 0
    stack = []

    for i in moves:
        for j in range(len(board)):
            if board[j][i - 1] != 0:
                stack.append(board[j][i - 1])
                board[j][i - 1] = 0

                if len(stack) > 1 and stack[-1] == stack[-2]:
                    answer += 2
                    stack.pop(-1)
                    stack.pop(-1)

                break

    return answer


if __name__ == '__main__':
    board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
    moves = [1, 5, 3, 5, 1, 2, 1, 4]

    print(solution(board, moves))
    print(another_solution(board, moves))
