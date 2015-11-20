import sys

ids = list()
cnt = 0
for line in open(sys.argv[2]):
    ids.append(','.join(line.strip().split('\t')))
    cnt += 1
    if cnt == int(sys.argv[1]):
        print(','.join(ids))
        ids = list()
        cnt = 0
print(','.join(ids))
