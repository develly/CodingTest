import datetime


def solution(a, b):
    ans = ['FRI', "SAT", 'SUN', 'MON', "TUE", 'WED', 'THU']

    days = b
    if a != 1:
        for i in range(a - 1, 0, -1):
            if i in [1, 3, 5, 7, 8, 11]:
                days += 31
            elif i in [4, 6, 9, 10, 12]:
                days += 30
            else:
                days += 29

    return ans[days % 7 - 1]


def shorten(a, b):
    """Summarize the code in one line."""
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return day[(sum(month[:a - 1]) + b - 1) % 7]


def use_datetime(a, b):
    ans = 'MON TUE WED THU FRI SAT SUN'.split()
    return ans[datetime.datetime(2016, a, b).weekday()]


if __name__ == '__main__':
    print(solution(5, 24))
    print(shorten(5, 24))
    print(use_datetime(5, 24))
