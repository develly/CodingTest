# coding=utf-8
def solution(s):
    """
        문제 해석
            x와 x가 아닌 다른 글자들이 나온 횟수
            -> aaabbaccccabba 에서는 x는 a이고, 그 다음 글자 부터 a인가 a가 아닌가로 구분
            -> 따라서, a의 갯수와 a가 아닌 단어의 갯수가 일치할 때 과정을 중지하고 단어를 분리함
            -> 예시) abaabc 라면 a-1개, b-1개, (중지), a-2개, bc-2개 (중지)
    """
    answer = 0
    x = ""
    x_cnt = 0
    not_x_cnt = 0
    cp = s
    for i in s:
        if x == "" or x == i:
            x = i
            x_cnt += 1
            continue
        else:
            not_x_cnt += 1

        if x_cnt == not_x_cnt:
            cp = cp[2 * x_cnt:]
            x = ""
            x_cnt, not_x_cnt = 0, 0
            answer += 1

    return answer + 1 if cp else answer


if __name__ == '__main__':
    print(solution("banana"))
    print(solution("abracadabra"))
    print(solution("aaabbaccccabba"))


