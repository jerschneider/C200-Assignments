def longlen(*strings):
    max = 0
    for s in strings:
        if len(s) > max:
            max = len(s)

    return max