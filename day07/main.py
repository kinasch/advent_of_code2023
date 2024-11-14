from functools import cmp_to_key

f = open("./input", "r")
lines = f.read().split('\n')

labels = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
labels.reverse()

# Returns the type of hand out of the possible 7: 0-6
def get_type(h):
    for i,label in enumerate(labels):
        ct = h.count(label)
        #print(h,label,ct)
        if ct==0 or ct==1:
            continue
        if ct == 2:
            # full house with 2 beginning
            for l_fh in labels[i+1:]:
                if h.count(l_fh) == 3:
                    return 4
            # two pair
            for l_tp in labels[i+1:]:
                if h.count(l_tp) == 2:
                    return 2
            return 1
        # three of a kind
        if ct==3:
            # full house with 3 beginning
            for l_fh in labels[i+1:]:
                if h.count(l_fh) == 2:
                    return 4
            return 3
        # 4 and 5 of a kind (e.g. 5 is rank 6)
        return ct+1
    # highest card
    return 0

# Compare function to compare hands in the form of [hand,type,bet]  
def compare_for_hand(item1, item2):
    if item1[1] < item2[1]:
        return -1
    elif item1[1] > item2[1]:
        return 1
    else:
        for i in range(5):
            if item1[0][i] == item2[0][i]:
                continue
            return labels.index(item1[0][i])-labels.index(item2[0][i])
        return 0

hands = []
for line in lines:
    hand = line.split(" ")
    hands.append([hand[0],get_type(hand[0]),int(hand[1])])

#print(hands)

sorted_hands = sorted(hands, key=cmp_to_key(compare_for_hand))

print("1st star solution: ", sum([w[2]*(i+1) for i,w in enumerate(sorted_hands)]) )