import sys

#prime = open('history_prime.csv')
if len(sys.argv) > 1:
    hist_file = sys.argv[1]
else:
    hist_file = 'history_out.csv'
total = 0.0
#food_total = 0.0
cat_list = [['total'], [0.0],[0]]
pri_entries = 0

with open(hist_file) as f:
    for line in f:
        line_list = line.strip().split(',')
        if len(line_list) < 2:
            continue
        if "invest" in line_list[2]:
            continue
        value = float(line_list[1])
        #if "food" in (line):
        #    food_total += value
        if len(line_list) > 2:
            for n in range(2,len(line_list)):
                #print(n)
                #print(line_list)
                if line_list[n] in cat_list[0]:
                    index = cat_list[0].index(line_list[n])
                    cat_list[1][index] += value
                else:
                    cat_list[0].append(line_list[n])
                    cat_list[1].append(value)
                    cat_list[2].append(n-1)
        total += value
        cat_list[1][0] += value

#for j in range(max(cat_list[2])+1):
j = 1
for i in range(len(cat_list[0])):
    if cat_list[2][i] == j and cat_list[1][i] < 0:
        print(cat_list[0][i] + ': $' +  '{0:.2f}'.format(cat_list[1][i] * -1) +',' +  '{0:.2f}'.format(cat_list[1][i] * -1))
        if j == 1:
             pri_entries += 1

print(pri_entries)
