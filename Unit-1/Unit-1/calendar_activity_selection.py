"""Calendar-like event selection using the Greedy strategy.

This is an educational activity-selection example, not Google's internal
calendar scheduling algorithm. No external packages are required.
"""


def select_compatible_events(events):
    """Select a maximum-size compatible set for classic activity selection.

    Each event is a dictionary with 'name', 'start', and 'finish' fields.
    An event may start at the same time the previously selected event finishes.
    """
    sorted_events = sorted(events, key=lambda event: event["finish"])
    selected = []
    last_finish = None

    for event in sorted_events:
        if last_finish is None or event["start"] >= last_finish:
            selected.append(event)
            last_finish = event["finish"]

    return sorted_events, selected


def display_events(title, events):
    print(f"\n{title}")
    print("-" * 48)
    if not events:
        print("No events.")
        return

    print(f"{'Event':<22} {'Start':>8} {'Finish':>10}")
    print("-" * 48)
    for event in events:
        print(
            f"{event['name']:<22} "
            f"{event['start']:>8} "
            f"{event['finish']:>10}"
        )


def main():
    events = [
        {"name": "Study", "start": 9, "finish": 10},
        {"name": "Team meeting", "start": 9, "finish": 11},
        {"name": "Lab", "start": 10, "finish": 12},
        {"name": "Lunch appointment", "start": 12, "finish": 13},
        {"name": "Club activity", "start": 11, "finish": 14},
        {"name": "Revision", "start": 13, "finish": 15},
    ]

    sorted_events, selected = select_compatible_events(events)
    selected_ids = {id(event) for event in selected}
    not_selected = [
        event for event in sorted_events if id(event) not in selected_ids
    ]

    display_events("All events (sorted by finish time)", sorted_events)
    display_events("Selected compatible events", selected)
    display_events("Events not selected in this schedule", not_selected)

    print("\nNote: time values are simple integer units (for example, 9 = 9:00).")
    print("This is a simplified educational activity-selection model.")


if __name__ == "__main__":
    main()
