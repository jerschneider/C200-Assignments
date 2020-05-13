def s():
    return 1

def tom():
    return 0

def cam(X):
    return X

def h():
    return 2

def tom(x): # overwrites previous tom
    return h() + x

def g():
    pass

def j(who, what, when):
    temp = who * what
    temp = when - temp
    return temp

print(s)
print(s())
print(h() + cam(s()))
print(j(2, 3, -4) - tom(h()))
print(g())
