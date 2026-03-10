def game_event_stream() -> None:
    players = [
        ("alice", 5, "killed monster"),
        ("bob", 12, "found treasure"),
        ("charlie", 8, "leveled up"),
        ("david", 15, "killed monster"),
        ("eve", 11, "found treasure")
    ]

    for i in range(1000):
        player = players[i % len(players)]
        yield player


def fibonacci() -> None:
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b


def primes() -> None:
    num = 2
    while True:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
        num += 1


def main() -> None:
    print("=== Game Data Stream Processor ===\n")
    print("Processing 1000 game events...\n")

    stream = game_event_stream()

    total = 0
    high_level = 0
    treasure = 0
    level_up = 0

    event_id = 1

    for event in stream:
        name, level, action = event

        if event_id <= 3:
            print(f"Event {event_id}: Player {name} (level {level}) {action}")

        total += 1

        if level >= 10:
            high_level += 1
        if action == "found treasure":
            treasure += 1
        if action == "leveled up":
            level_up += 1

        event_id += 1
    print("...")
    print("\n=== Stream Analytics ===")
    print("Total events processed:", total)
    print("High-level players (10+):", high_level)
    print("Treasure events:", treasure)
    print("Level-up events:", level_up)

    print("\nMemory usage: Constant (streaming)")

    print("\n=== Generator Demonstration ===")

    fib = fibonacci()
    print("Fibonacci sequence (first 10):", end=" ")
    for _ in range(10):
        print(next(fib), end=" ")

    print()

    prime = primes()
    print("Prime numbers (first 5):", end=" ")
    for _ in range(5):
        print(next(prime), end=" ")

    print()


if __name__ == "__main__":
    main()
