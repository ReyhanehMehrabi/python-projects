# Imagine you get a list such as [(1982, 2023),(1950, 2010),(1960, 2015),...]
# Find the year with most people alive


years_list = [(1982, 2023), (1950, 2010), (1960, 2015)]

max_age = 0
max_index = None

for i, life_period in enumerate(years_list):
    age = life_period[1] - life_period[0]
    if age > max_age:
        max_age = age
        max_index = i
print(
    f"maximum age is {max_age} years, for persion with life period of: {years_list[max_index]}")
