data_parent = [
    ("alya", "bima"),
    ("alya", "satria"),
    ("bima", "david"),
    ("bima", "emma"),
    ("satria", "yunita"),
    ("satria", "grace"),
]

def get_sibling(target) :
    parents = [p for p, c in data_parent if c == target]
    siblings = set ()
    for p in parents:
        children = [c for parents, c in data_parent if parents == p and c != target]
        siblings.update(children)
    return list (siblings)

def get_grandparents(target_cucu):
    results = []
    parents = [p for p, c in data_parent if c == target_cucu]
    for p in parents:
        grandparents = [gp for gp, child in data_parent if child == p]
        results.extend(grandparents)
    return results

print(f"Saudara Bima: {get_sibling('bima')}")
print(f"Kakek/Nenek Emma: {get_grandparents('emma')}")