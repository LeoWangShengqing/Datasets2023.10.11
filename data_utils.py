def readList(list_path, ignore_head=False, sort=True):
    lists = []
    with open(list_path) as f:
        lists = f.read().splitlines()
    if ignore_head:
        lists = lists[1:]
    if sort:
        lists.sort()
    return lists


def capitalize_first(s):
    return s[0].upper() + s[1:]
