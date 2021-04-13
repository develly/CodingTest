def solution(n, lost, reserve):
    answer = 0
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)

    for i in set_reserve:
        if i - 1 in set_lost:
            set_lost.remove(i-1)
        elif i + 1 in set_lost:
            set_lost.remove(i+1)
    return n - len(set_lost)

if __name__ == "__main__":
    n, lost, reserve = 5, [2, 4], [1, 3, 5]
    answer = solution(n, lost, reserve)	
    print(answer)