#-*- encoding: utf-8 -*-
# K번째 수

# solution 1 
def solution(array, commands):
    answer = []
    for i,j,k  in commands:
        answer.append(sorted(array[i-1:j])[k-1])
    return answer

# solution 2 
def solution2(array, commands):
    answer = []
    for i, j, k in commands:
        target = array[i-1:j]
        target.sort()
        answer.append(target[k-1])
    return answer

if __name__ == "__main__":
    array = [1, 5, 2, 6, 3, 7, 4]	
    commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
    answer = solution(array, commands)
    print(answer)