# Imports
import sys

f = open("./"+sys.argv[1], "r")
lines = f.read().split('\n')

commands = list(lines[0])
nodes = {}

for l in lines[2:]:
    cur_line = l.split("=")
    key = cur_line[0][:-1]
    nodes[key] = {}
    values = cur_line[1].replace(" ","").replace("(","").replace(")","").split(",")
    nodes[key]["L"], nodes[key]["R"] = values[0], values[1]

cur_key = "AAA"
counter = 0
amount_of_commands = len(commands)
while cur_key != "ZZZ":
    cur_key = nodes[cur_key][commands[counter%amount_of_commands]]
    counter = (counter+1)

print("1st star:",counter)

# 2nd key
cur_key = [x for x in nodes.keys() if x[2] == "A"]
counter = 0
amount_of_commands = len(commands)
while True:
    if False not in [x[2] == "Z" for x in cur_key]:
        break
    cur_key = [ nodes[y][commands[counter%amount_of_commands]] for y in cur_key ]
    counter = (counter+1)

print("2nd star:",counter)