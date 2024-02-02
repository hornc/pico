#!/usr/bin/env python3

"""
This Python script generates a bf script which generates Python scripts based on Pico scripts.
"""


PRE = """T, P, C = {}, 0, 0

def pico(*a):
    global T, P, C
    r, T[P], P, C = (lambda x: (*x, x[0] != 0) if len(x) > 2 else (None, *(max(0, v) for v in x), 0))(([
        lambda a,v: ((2 * C - 1) * (not len(a)) or (len(a) < 2 and a[0] + a[0]//abs(a[0])) or (a, 0)[a[0] < 0], v, P),
        lambda a,v: (1 - v if a[1] == 1 else v + 2 * a[1] - 5, P),
        lambda a,v: (v, P - 1),
        lambda a,v: (v, P + 1),
        lambda a,v: (v, print([bool, int, chr][a[1] - 1](v), end='') or P),
        lambda a,v: ([bool, int, lambda s: s and ord(s[0]) or 0][a[1] - 1](input('>')), P)
    ][((len(a) < 2) or (max(1, 0 - a[0]))) - 1](a, T.get(P, 0))))
    if r != 0: return r
    while (bool(T.get(P, 0)) == a[1][r] - 1 and ([pico(-c, a) for c,a in a[1][2:]] or 1)): r = 1


"""

PICO  = 'pico('
CLOSE = '),'

def p(current, target, d=0):
    """
    print:
    Go from current to target,
    change the cell value by d
    and output the cell as ASCII.
    """
    set_cell(current, target, d)
    print('.', end='')
    return target


def set_cell(current, target, d=0):
    """
    go:
    Go from current to target,
    change the cell value by d.
    """
    c = '+' if d > 0 else '-'
    s = '>' if current < target else '<'
    print(s * abs(current - target) + c * abs(d), end='')
    return target


def reset_points(pos, points):
    pos = set_cell(pos, 2,  48 - points[0])
    pos = set_cell(pos, 3,  78 - points[1])
    pos = set_cell(pos, 4, 108 - points[2])
    points = [48, 78, 108]
    return pos, points


# set up some ASCII points...

points = [48, 78, 108]

# 10, 32, 48, 78, 108
CODE = """++++[>++++++++<-]
++++++[>>++++++++>+++++++++++++>++++++++++++++++++<<<<-]
++++++++++"""

# start on 10 

pos = 0

print(CODE)

for c in PRE:
    n = ord(c)
    if n == 32:
        pos = p(pos, 1)
    elif n == 10:
        pos = p(pos, 0)
    elif n == 9:
        pos = p(pos, 0, -1)
    else:
        offs = (n - 32) // 32
        pos = p(pos, offs + 2, n - points[offs])
        points[offs] = n


# reset points to a known point  [48, 78, 108]
pos, points = reset_points(pos, points)

# do the pico transducing:

# set up [] flags at pos 6
pos = p(pos, 6) 

print('>+<')

# read input loop
print(',[<')

# 91 = [
# 93 = ]

print('+++++++[>-------------<-]>') # subtract 91 (for ord('['))
print('[>->+<<--[>>-<<[-]]]')

# output pico( if we need to
print('>[')
pos = 7

for c in PICO:
    n = ord(c)
    offs = (n - 32) // 32
    pos = p(pos, offs + 2, n - points[offs])
    points[offs] = n

pos, points = reset_points(pos, points)
pos = set_cell(pos, 7)
print('[-]]>[')
pos = 8

# output ), if we need to
for c in CLOSE:
    n = ord(c)
    offs = (n - 32) // 32
    pos = p(pos, offs + 2, n - points[offs])
    points[offs] = n
pos, points = reset_points(pos, points)
pos = set_cell(pos, 8)

# set up first flag and get new input before repeating main transducer loop
print('[-]]<+<,]')

