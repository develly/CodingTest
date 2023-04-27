def solution(cards1, cards2, goal):
    for i in goal:
        if len(cards1) != 0 and i == cards1[0]:
            cards1.remove(i)
        elif len(cards2) != 0 and i == cards2[0]:
            cards2.remove(i)
        else:
            return "No"
    return "Yes"


if __name__ == '__main__':
    card1 = ["i", "drink", "water"]
    card2 = ["want", "to"]
    goal = ["i", "want", "to", "drink", "water"]

    print(solution(card1, card2, goal))
