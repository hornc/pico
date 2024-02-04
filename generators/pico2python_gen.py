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

# Init cells:
# 10, 32, 48, 78, 108
INIT = """++++[>++++++++<-]
++++++[>>++++++++>+++++++++++++>++++++++++++++++++<<<<-]
++++++++++"""


def p(current, target, d=0):
    """
    print:
    Go from current to target,
    change the cell value by d
    and output the cell as ASCII.
    """
    g(current, target, d)
    print('.', end='')
    return target


def g(current, target, d=0):
    """
    go:
    Go from current to target,
    change the cell value by d.
    """
    c = '+' if d > 0 else '-'
    s = '>' if current < target else '<'
    end = '' if d <= 12 else '\n'
    print(s * abs(current - target) + c * abs(d), end=end)
    return target


def reset_points(pos, points):
    pos = g(pos, 2,  48 - points[0])
    pos = g(pos, 3,  78 - points[1])
    pos = g(pos, 4, 108 - points[2])
    points = [48, 78, 108]
    return pos, points


def output_str(s, pos, points):
    """
    Generate bf code to output string s
    give points and a current pos.
    """
    for c in s:
        n = ord(c)
        if n == 32:
            pos = p(pos, 1)
        elif n == 10:
            pos = p(pos, 0, 0)
        elif n == 9:
            pos = p(pos, 0, -1)
            print('+')
        else:
            offs = (n - 32) // 32
            pos = p(pos, offs + 2, n - points[offs])
            points[offs] = n
    # reset points to a known point [48, 78, 108]
    return reset_points(pos, points)


def main():
    # set up some ASCII points...
    print(INIT)
    points = [48, 78, 108]

    # start on 10
    pos = 0

    # Unconditionally output the Pico primer:
    pos, points = output_str(PRE, pos, points)

    # Do the pico transducing:
    # set up [] flags at pos 6
    pos = g(pos, 6)

    print('>+<')

    # read input loop
    print(',[<')

    # 91 = [
    # 93 = ]

    print('+++++++[>-------------<-]>')  # subtract 91 (for ord('['))
    print('[>->+<<--[>>-<<[-]]]')

    # output pico( if we need to
    print('>[')
    pos = 7

    pos, points = output_str(PICO, pos, points)
    pos = g(pos, 7)
    print('[-]]>[')
    pos = 8

    # output ), if we need to
    pos, points = output_str(CLOSE, pos, points)
    pos = g(pos, 8)

    # set up first flag and get new input before repeating main transducer loop
    print('[-]]<+<,]')

if __name__ == '__main__':
    main()
