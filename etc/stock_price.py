def solution(prices):
    answer = [0] * len(prices)

    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer

if __name__ == "__main__":
    prices = [1, 2, 3, 2, 3]	
    answer = solution(prices)
    print(answer)
