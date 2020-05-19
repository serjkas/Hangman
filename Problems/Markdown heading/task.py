def heading(l_a, l_b=None):
    if l_b is None or l_b < 1:
        return '#' + " " + l_a
    elif l_b > 6:
        return '#' * 6 + " " + l_a
    else:
        return '#' * int(l_b) + " " + l_a
