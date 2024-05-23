def compare(a, b):
    if a is None and b is None:
        return True

    if a is None or b is None:
        return False

    if a.value != b.value:
        return False

    return compare(a.left, b.left) and compare(a.right, b.right)
