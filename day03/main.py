import re

# Returns the surrounding objects of a matrix and their positions.
def surrounding(i, j, mat):
    max_i = len(mat)
    max_j = len(mat[0])
    ret = []
    for ii in range(max(0, i-1), min(i+2, max_i)):
        for jj in range(max(0, j-1), min(j+2, max_j)):
            if (ii, jj) == (i, j):
                continue
            ret.append([mat[ii][jj],[ii,jj]])
    return ret

# Read in the file "input" containing your input.
f = open("./input", "r")
lines = f.read().split('\n')
field = []

# Split lines into 'char' arrays (still strings in python)
number_indices = []
count = 0
for line in lines:
    field.append([*line])

    # Go through every instance of numbers in the current line
    for iter in re.finditer(r"\d{1,3}",line):
        (x,y) = iter.span()
        number_indices.append([[count,yy] for yy in range(x,y)])
    count += 1

sum = 0
valid = False
gears = {}
for i in range(len(number_indices)):
    for j in range(len(number_indices[i])):
        # Search through the surrounding elements for a symbol other than a number or "."
        for sur in surrounding(number_indices[i][j][0],number_indices[i][j][1],field):
            # If the current object of the surrounding objects is a number or a dot, skip it
            if (re.search(r"\d",sur[0]) or re.search(r"\.",sur[0])):
                continue
            # Should the surrounding object be a star, save it to the gears
            if sur[0] == "*":
                temp_text = re.sub(r"[\[\] ]","",str(sur[1]))
                # Create a new dictionary entry if it does not exist yet.
                if not (temp_text in gears):
                    gears[temp_text] = []
                # Append the current number to the existing numbers on that gear.
                gears[temp_text].append(int("".join([field[x[0]][x[1]] for x in number_indices[i]])))
            # Mark the number as valid, to ignore its other digits.
            valid = True
            break
        # Add the whole number to the sum of numbers that are part numbers.
        if valid:
            sum += int("".join([field[x[0]][x[1]] for x in number_indices[i]]))
            break
    valid = False
        
print("1st star solution: "+str(sum))

gear_product = 0
for key in gears.keys():
    if len(gears[key]) == 2:
        gear_product += (gears[key][0]*gears[key][1])

print("2st star solution: "+str(gear_product))