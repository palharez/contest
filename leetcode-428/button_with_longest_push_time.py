from typing import List


def button_with_longest_push_time(events: List[List[int]]) -> int:
    maximum = [events[0][0], events[0][1]]

    for i in range(1, len(events)):
        push_time = abs(events[i - 1][1] - events[i][1])
        if push_time > maximum[1] or (
            push_time == maximum[1] and events[i][0] < maximum[0]
        ):
            maximum = [events[i][0], push_time]

    return maximum[0]


if __name__ == "__main__":
    events = [[1, 2], [2, 5], [3, 9], [1, 15]]
    assert button_with_longest_push_time(events=events) == 1
    events = [[10, 5], [1, 7]]
    assert button_with_longest_push_time(events=events) == 10
    events = [[10, 4], [1, 6], [7, 14]]
    assert button_with_longest_push_time(events=events) == 7
    events = [[9, 4], [19, 5], [2, 8], [3, 11], [2, 15]]
    assert button_with_longest_push_time(events=events) == 2
    events = [[12, 2], [8, 3], [18, 5], [4, 6], [3, 7], [1, 9], [2, 17], [18, 20]]
    assert button_with_longest_push_time(events=events) == 2
