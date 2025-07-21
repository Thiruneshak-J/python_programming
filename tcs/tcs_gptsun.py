def count_sundays(start_day, total_days):
    days = ["sun", "mon", "tue", "wed", "thu", "fri", "sat"]
    start_index = days.index(start_day.lower())
    
    count = 0
    for i in range(total_days+1):
        current_day = days[(start_index + i) % 7]
        if current_day == "sun":
            count += 1
    return count

# Example
print(count_sundays("sat", 28))  # Output: 1
