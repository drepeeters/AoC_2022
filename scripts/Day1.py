#import data
path = "C:/Users/drepeeters/PycharmProjects/AoC/files/day1.txt"
data = []
with open(path, 'r') as fp:
    for file in fp:
        data.append(file.rstrip('\n'))

# Day 1 first assignment
calorie_counter = {}
elf_counter = 0
for calories in data:
    if calories == '':
        elf_counter += 1
    else:
        calorie_counter[elf_counter] = int(calories) + int(calorie_counter.get(elf_counter, 0))

max_elf = max(calorie_counter, key=calorie_counter.get)
print(f"Elf {max_elf} has the highest calories with {calorie_counter[max_elf]} calories")


# Day 1 second assignment
def top_n_calories(list_of_calories: list, n: int):
    sorted_calories = sorted(list_of_calories, reverse=True)
    return sum(sorted_calories[0:n])


total_calories = [calorie for calorie in calorie_counter.values()]
n = 3
total_calories = top_n_calories(total_calories, n=n)
print(f"Total calories of {n} Elves: {total_calories}")
