from array import array
import re

f = open("./input", "r")
lines = f.read().split('\n')

# 1st star
sum = 0
def first_star(lines):
    sum = 0
    for line in lines:
        # Remove the "Card DDD:" from every line
        line = re.sub(r"Card.*:","",line)
        # Create an exponent, initialize with -1 to increase to 0 as the first number. (2^0)=1
        exponent = -1
        number_sides = line.split("|")
        # Go through all of "your numbers" on the right side of the '|'
        for y_n in re.findall(r"\b\d+\b",number_sides[1]):
            # If there is a match for the current number on the winning numbers side, increase the exponent.
            if re.search(r"\b"+y_n+r"\b",number_sides[0]):
                exponent += 1
        # If the exponent is greater than or equal zero (at least one number matched), increase the sum by 2^exponent.
        #   Because if the one point you get for one winning number is doubled everytime you get another winning number,
        #   it is basically the powers for 2.
        if exponent >= 0:
            sum += (2**exponent)
    return sum

sum = first_star(lines)
print("1st star solution: "+str(sum))

# 2nd star
def second_star(lines):
    number_of_cards = 0
    cards = [1] * len(lines)
    for i in range(len(cards)):
        for cur_line in ([lines[i]] * cards[i]):
            number_of_cards += 1
            cur_line = re.sub(r"Card.*:","",cur_line)
            number_sides = cur_line.split("|")
            counter = 1
            for y_n in re.findall(r"\b\d+\b",number_sides[1]):
                if re.search(r"\b"+y_n+r"\b",number_sides[0])and i+counter < len(cards):
                    cards[i+counter] += 1
                    counter += 1
    return number_of_cards

sum = second_star(lines)
print("2nd star solution: "+str(sum))