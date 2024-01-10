import re

f = open("./input", "r")
lines = f.read().split('\n')

# 1st star
sum = 1
times = [int(t) for t in re.findall(r"\b\d+\b",lines[0])]
distances = [int(d) for d in re.findall(r"\b\d+\b",lines[1])]

for i in range(len(times)):
    count = 0
    # print(times[i],distances[i])
    for j in range(times[i]):
        if j*(times[i]-j) > distances[i]:
            count += 1
    print(count)
    sum *= count

print(f"1st star solution: {sum}")

# 2nd star
sum = 0
race_time = int(re.sub(r"[^0-9]","",lines[0]))
race_distance = int(re.sub(r"[^0-9]","",lines[1]))

for i in range(race_time):
    if i * (race_time-i) > race_distance:
        sum += 1

print(f"2nd star solution: {sum}")