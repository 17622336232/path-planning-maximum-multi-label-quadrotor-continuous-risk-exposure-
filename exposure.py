"""Compare total time in a region with its longest uninterrupted visit."""

def exposure_times(segments):
    """Return total and longest exposure in seconds for (duration, inside) pairs."""
    total = current = longest = 0
    for duration, inside in segments:
        if duration < 0:
            raise ValueError("Segment duration must be nonnegative")
        if duration == 0:
            continue
        if inside:
            current += duration
            total += duration
            longest = max(longest, current)
        else:
            current = 0
    return total, longest


if __name__ == "__main__":
    routes = {
        "A": [(4, True)],
        "B": [(2, True), (1, False), (2, True)],
    }
    for name, segments in routes.items():
        total, longest = exposure_times(segments)
        print(f"Route {name}: total {total} s, longest visit {longest} s")
