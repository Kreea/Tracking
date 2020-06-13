import sys

#prime = open('history_prime.csv')
if len(sys.argv) > 1:
    hist_file = sys.argv[1]
else:
    hist_file = 'history_out.csv'
total = 0.0 #Actually not used. cat_list[1][0] contains the total that gets printed
#food_total = 0.0
cat_list = [['total'], [0.0],[0]] #The order here is name of cat, value, and cat tier

with open(hist_file) as f:
    for line in f:
        line_list = line.strip().split(',')
        if len(line_list) < 2:
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
                    cat_list[1][index] = round(cat_list[1][index],2)
                else:
                    cat_list[0].append(line_list[n])
                    cat_list[1].append(value)
                    cat_list[2].append(n-1)
        total += value
        total = round(total,2)
        cat_list[1][0] += value
        cat_list[1][0] = round(cat_list[1][0],2)

print('-----------')
for j in range(max(cat_list[2])+1):
    for i in range(len(cat_list[0])):
        if cat_list[2][i] == j:
            #print(cat_list[0][i] + ": " + '{0:.2f}'.format(cat_list[1][i])+ ", " + str(cat_list[2][i]))
            print(cat_list[0][i] + ": " + '{0:.2f}'.format(cat_list[1][i]))
    print('-----------')

