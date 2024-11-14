import re

f = open("./input", "r")
lines = f.read().split('\n')


def find_in_map(k,n):
    for line in maps[k]:
        if n >= line[1] and n < (line[1]+line[2]):
            return line[0]+(n-line[1])
    return n

# 1st star
seeds = []
maps = {"seed-to-soil":[],
        "soil-to-fertilizer":[],
        "fertilizer-to-water":[],
        "water-to-light":[],
        "light-to-temperature":[],
        "temperature-to-humidity":[],
        "humidity-to-location":[]}

cur_key = ""
for line in lines:
    if line=="":
        continue
    if seeds == []:
        seeds = [int(x) for x in re.findall(r"\b\d+\b",line)]
        continue
    if line.find("-") != -1:
        for key in maps.keys():
            if line.find(key) != -1:
                cur_key = key
                break
    else:
        maps[cur_key].append([int(x) for x in re.findall(r"\b\d+\b",line)])

smallest_location = 10**10
for seed in seeds:
    cur_num = seed
    for key in maps.keys():
        cur_num = find_in_map(key,cur_num)
        # print(seed,key,cur_num)
    if cur_num < smallest_location:
        smallest_location = cur_num

# print(seeds, maps)
print(f"1st star solution: {smallest_location}")


# 2nd star
maps = {"seed-to-soil":[],
        "soil-to-fertilizer":[],
        "fertilizer-to-water":[],
        "water-to-light":[],
        "light-to-temperature":[],
        "temperature-to-humidity":[],
        "humidity-to-location":[]}

cur_key = ""
for line in lines[2:]:
    if line=="":
        continue
    if line.find("-") != -1:
        for key in maps.keys():
            if line.find(key) != -1:
                cur_key = key
                break
    else:
        maps[cur_key].append([int(x) for x in re.findall(r"\b\d+\b",line)])

print(maps["seed-to-soil"][2])

smallest_location = 10**10
seeds = [int(x) for x in re.findall(r"\b\d+\b",lines[0])]
for i in range(0,len(seeds)-1,2):
    print(seeds[i],seeds[i+1])
    for j in range(seeds[i],seeds[i]+seeds[i+1]):
        tj = j
        for key in maps.keys():
            tj = find_in_map(key,tj)
            #print(j,key,tj)
        if tj < smallest_location:
            smallest_location = tj
    print("seeds for: "+str(i))

# print(seeds, maps)
print(f"2nd star solution: {smallest_location}")