# hash, 완주하지 못한 선수

def solution(participant, completion):
    answer = ''
    tmp = 0
    dic = {}

    for name in participant:
        hash_value = hash(name)
        tmp += hash_value
        dic[hash_value] = name

    for name in completion:
        hash_value = hash(name)
        tmp -= hash_value
      
    answer = dic[tmp]
    return answer

if __name__ == "__main__":
    answer = solution(['a','b','c'], ['b', 'a'])
    print(answer)
