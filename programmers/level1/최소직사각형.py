def solution(sizes):
    width = 0
    height = 0

    for card in sizes:
        width = max(width, max(card))
        height = max(height, min(card))

    return width * height


def shortcut(sizes):
    """Summarize the code in one line."""
    return max(max(card) for card in sizes) * max(min(card) for card in sizes)


if __name__ == '__main__':
    print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
    print(shortcut([[60, 50], [30, 70], [60, 30], [80, 40]]))
