import random


temperatures = []
for _ in range(7):
    temperature = random.randint(26, 40)
    temperatures.append(temperature)

# Step 2: Define days of the week
days_of_the_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

good_days = []
for i in range(7):
    if temperatures[i] % 2 == 0:
        good_days.append(days_of_the_week[i])

highest_temp = temperatures[0]
highest_temp_day = days_of_the_week[0]
for i in range(1, 7):
    if temperatures[i] > highest_temp:
        highest_temp = temperatures[i]
        highest_temp_day = days_of_the_week[i]


lowest_temp = temperatures[0]
lowest_temp_day = days_of_the_week[0]
for i in range(1, 7):
    if temperatures[i] < lowest_temp:
        lowest_temp = temperatures[i]
        lowest_temp_day = days_of_the_week[i]


total_temp = sum(temperatures)
average_temp = total_temp / 7


above_avg = []
for temp in temperatures:
    if temp > average_temp:
        above_avg.append(temp)

# Step 8: Print the weather report
print("Weather Report:")
print("---------------")
print(f"Temperatures for the week: {temperatures}")
print(f"Good days for Shelly: {good_days}")
print(f"Highest temperature: {highest_temp}°C on {highest_temp_day}")
print(f"Lowest temperature: {lowest_temp}°C on {lowest_temp_day}")
print(f"Average temperature: {average_temp:.2f}°C")
print(f"Days with temperatures above average: {above_avg}")
