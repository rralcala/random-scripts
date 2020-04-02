
def parse_passwd_file(filename):
    user_f = open(filename, 'r')
    lines = {}
    for line in user_f:
        line = line.split('#')[0]
        if len(line) > 0:
            elements = line.rstrip().split(':')
            id = elements[2]
            lines[id] = elements
    return lines


if __name__ == "__main__":
    users = parse_passwd_file('/etc/passwd')
    groups = parse_passwd_file('/etc/group')

    keep = set()
    for k, v in groups.items():
        if len(v[3]) > 0:
            keep.add(k)

    for k,v in users.items():
        keep.add(v[3])

    for i in keep:
        if i in groups:
            print(groups[i][0])
