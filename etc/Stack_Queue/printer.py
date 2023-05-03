#-*- encoding: utf-8 -*-
# 프린터
def doPrint(i, priorities):
    for num in priorities[1:]:
        if priorities[i] < num:
            return False
    return True

def solution(priorities, location):
    answer = 0
    prioity = priorities[location]
    
    while True:
        if doPrint(0, priorities):
            answer += 1
            priorities.pop(0)
            if not location: # 0
                break
            else :
                location -= 1
        else :
            priorities.append(priorities.pop(0))
            if not location: # 0
                location = len(priorities) - 1
            else :
                location -= 1
        
    return answer

if __name__ == "__main__":
    priorities = [2, 1, 3, 2]	
    location = 2
    answer = solution(priorities, location)
    print(answer)