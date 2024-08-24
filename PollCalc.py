import csv

votes = []
with open('votes.csv', newline='') as f:
    reader = csv.reader(f)
    votes = list(reader)

for vote in votes:
    if len(vote) == 0: votes.remove(vote)
    continue
    for string in vote:
        if '#' in string: votes.remove(vote)
        break

totals = {}
index = []
count = 0
index_counted = False

for vote in votes:
    if not index_counted:
        for choice in vote:
            totals[choice] = 0
        index = list(totals.keys())
        index_counted = True
        continue
    count += 1
    i = 0
    for choice in vote:
        totals[index[i]] += float(choice)
        i += 1

for choice in totals.keys():
    totals[choice] /= count

sorted_totals = dict(sorted(totals.items(), key=lambda item: item[1], reverse=True))

sorted_index = list(sorted_totals.keys())
runoff = {
    sorted_index[0]: 0,
    sorted_index[1]: 0
}

index0_pos = 0
index1_pos = 0
count = 0
for i in index:
    if i == sorted_index[0]: 
        index0_pos = count
    if i == sorted_index[1]:
        index1_pos = count
    count += 1

for vote in votes:
    if vote[index0_pos] > vote[index1_pos]:
        runoff[sorted_index[0]] += 1
    elif vote[index0_pos] < vote[index1_pos]:
        runoff[sorted_index[1]] += 1

sorted_runoff = dict(sorted(runoff.items(), key=lambda item: item[1], reverse=True))

with open('output.txt', 'w') as f:
    f.write(f'Score results: {sorted_totals}\nRunoff results: {sorted_runoff}\n')
