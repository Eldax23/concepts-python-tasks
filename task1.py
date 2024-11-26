print("Number of Steps taken each day in a month: ")

i = 0
list = []
for i in range(10):
    steps = int(input(f"Day {i + 1} : "))
    list.append(steps)


maxSteps = max(list)
minSteps = min(list)
avgSteps = sum(list) / len(list)


print(f"Max Steps: {maxSteps}")
print(f"Min Steps: {minSteps}")
print(f"Average Steps: {avgSteps}")


list.sort(reverse=True)

print("the step count in descending order: ")

for i in list:
    print(f"{i} " , end= " ")

