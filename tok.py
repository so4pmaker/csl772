import sys

for line in sys.stdin:
    line = line.strip()
    print line
    line = line.replace("'s", " 's")
    line = line.replace("...", " ...")
    print len(line.split())
    for x in line.split():
        print x
