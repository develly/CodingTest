def solution(name, yearning, photo):
    answer = []
    for people in photo:
        score = 0
        for j in people:
            try:
                score += yearning[name.index(j)]
            except ValueError:
                continue
        answer.append(score)

    return answer


def shorten(name, yearning, photo):
    """Summarize the code in one line."""
    return [sum(yearning[name.index(j)] for j in people if j in name) for people in photo]


if __name__ == '__main__':
    name = ["may", "kein", "kain", "radi"]
    yearning = [5, 10, 1, 3]
    photo = [["may", "kein", "kain", "radi"], ["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]

    print(solution(name, yearning, photo))
    print(shorten(name, yearning, photo))
