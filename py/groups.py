
def parse(filename):
    user_f = open(filename,'r')
    lines = {}
    for line in user_f:
        line = line.split('#')[0]
        if len(line) > 0:
            elements = line.rstrip().split(':')
            id = elements[2]
            lines[id] = elements
    return lines

users = parse('/etc/passwd')
groups = parse('/etc/group')

keep = set()
for k,v in groups.items():
    if len(v[3]) > 0:
        keep.add(k)

for k,v in users.items():
    keep.add(v[3])

for i in keep:
    if i in groups:
        print groups[i][0]
