#-*- encoding: utf-8 -*-
# 위장
from collections import Counter
from functools import reduce

# solution 1 
def solution(clothes):
    kinds = [kind for name, kind in clothes]
    kind_dic = Counter(kinds)
    answer = reduce(lambda acc, cur: acc*(cur+1), kind_dic.values(), 1) - 1
    return answer

# solution 2
def solution2(clothes):
    dic = {}
    answer = 1
    
    for cloth in clothes:
        if hash(cloth[1]) not in dic.keys():
            dic[hash(cloth[1])] = []
        dic[hash(cloth[1])].append(cloth[0])
    
    for key in dic.keys():
        num = len(dic[key]) + 1
        answer = answer*num
    answer -= 1
    return answer

if __name__ == "__main__":
    clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
    answer = solution(clothes)	
    print(answer)