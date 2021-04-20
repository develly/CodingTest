#-*- encoding: utf-8 -*-
# n으로 표현

def solution(N, number):
    answer = 1
    result = [set() for x in range(9)]

    for i, factor in enumerate(result):
        if not i: continue
        result[i].add(int(str(N) * i))

    if N == number:
        return answer

    for index in range(2, 9):
        for j in range(1, index):  
            for x in result[j]:
                for y in result[index-j]:
                    result[index].add(x + y)
                    result[index].add(x - y)
                    result[index].add(x * y)
                    if y:
                        result[index].add(x // y)
            if number in result[index]:
                return index
    return -1

if __name__ == "__main__":
    N = 5
    number = 12
    answer = solution(N, number)
    print(answer)