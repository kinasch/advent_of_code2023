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

print(counter)