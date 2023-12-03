import re

def check_turns(content,allowed_balls):
    """ 
        Returns whether the maixmum amount of balls or less have been drawn in a turn.
    """
    for turn in content:
        for drawing in turn.split(","):
            n = int(re.sub(r"[a-z]*","",drawing).replace(" ",""))
            w = re.sub(r"\d+","",drawing).replace(" ","")
            if n > allowed_balls[w]:
                return False
    return True

def min_amount_of_balls(content):
    mins = {"red":0,"blue":0,"green":0}
    for turn in content:
        for drawing in re.split(r"[,;]",turn):
            n = int(re.sub(r"[a-z]*","",drawing).replace(" ",""))
            w = re.sub(r"\d+","",drawing).replace(" ","")
            if mins[w] < n:
                mins[w] = n
    return mins

f = open("./input", "r")
lines = f.read().split('\n')

# 1
id_sum = 0
for line_number in range(len(lines)):
    is_valid = False
    content = re.sub(r"Game \d+: ","",lines[line_number]).split(";")
    is_valid = check_turns(content,{"red":12,"green":13,"blue":14})
    if is_valid:
        id_sum += line_number+1
print("1st star solution: "+str(id_sum))

# 2
sum = 0
for line_number in range(len(lines)):
    content = re.sub(r"Game \d+: ","",lines[line_number]).split(";")
    mins = min_amount_of_balls(content)
    sum += (mins["red"]*mins["blue"]*mins["green"])
print("2st star solution: "+str(sum))