def solution(n): 
    ternery = ""
    answer = 0

    while n > 2:
        n, rest = divmod(n, 3)
        ternery += str(rest)

    ternery += str(n)   
    answer = int(ternery, 3)

    return answer

if __name__ == "__main__":
    n = 45
    answer = solution(n)
    print(answer)