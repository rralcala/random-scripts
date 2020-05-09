class Email:
    def __init__(self, title, ids, references, date):
        self.title = title
        self.id = ids
        self.references = references
        self.date = date
        self.childs = []


def parse_tree(emails):
    nodes = {}
    for email in emails:
        nodes[email.id] = email

    for email in emails:
        if len(email.references) == 1:
            nodes[email.references[0]].childs.append(email)
    return nodes


def print_tree(tree, d):
    for k, v in tree.items():
        print(f"{d} {v.title}")
        # sort(v.childs,) sort on date
        _print_tree(v, d + 1)


def _print_tree(tree, d):
    for v in tree.childs:
        print(f"{d} {v.title}")
        # sort(v.childs,) sort on date
        _print_tree(v, d + 1)


v1 = Email("Vacation", "1", [], "202001")
v2 = Email("Re: Vacation", "2", ["1"], "202002")
v3 = Email("Re: Vacation", "7", ["2"], "202002")
v4 = Email("Re: Vacation", "8", ["2"], "202002")
w1 = Email("Work", "4", [], "202003")
t = parse_tree([v1, v2, v3, v4, w1])
print_tree(t, 0)
