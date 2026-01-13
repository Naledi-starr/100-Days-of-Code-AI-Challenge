def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

data = [10, 20, 30, 40, 50]
average = calculate_average(data)
print(f"The average is: {average}")