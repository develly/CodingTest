def solution(name):
    answer = 0
    upDown = [min(ord(alphabet) - ord('A'), ord('Z') - ord(alphabet) + 1) for alphabet in name]
    index = 0
    
    while True:
        # calculate up down 
        answer += upDown[index]
        upDown[index] = 0

        # break point
        if sum(upDown) == 0:
            return answer
              
        # calculate right left
        right, left = 1, 1
        while upDown[index + right] == 0:
            right += 1
        while upDown[index - left] == 0:
            left += 1
        answer += min(right, left)

        # change index
        index += (-left) if right > left else right
        

# def solution(name):
#     answer = 0
#     cnt = 0
#     alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#     while True:

#         # up down
#         index = alphabet.index(name[cnt])
#         answer += min(index, len(alphabet) - index)
        
#         # break point
#         if cnt == len(name) - 1:
#             break
              
#         # right left
#         tmp = cnt
#         cnt += 1
#         while name[cnt] == 'A':
#             cnt += 1
#         answer += min(cnt - tmp, len(name) - cnt) 
        
#     return answer

if __name__ == "__main__":
    name = "JEROEN"
    answer = solution(name)
    print(answer)