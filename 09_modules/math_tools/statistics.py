def mean(numbers):
    if not numbers:
        raise ValueError("Cannot calculate mean of empty list")

    return sum(numbers) / len(numbers)


def maximum(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")

    return max(numbers)


def minimum(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")

    return min(numbers)