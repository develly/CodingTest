def solution(arr):
    answer = []
    cnt = 0
    for num in arr:
        if cnt == 0:
            answer.append(num)
            cnt += 1
        elif num != answer[-1]:
            answer.append(num)
        
    return answer

if __name__ == "__main__":
    arr = [1,1,3,3,0,1,1]
    answer = solution(arr)
    print(answer)
