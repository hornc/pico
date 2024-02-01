#!/bin/bash

# Pico to Python transducer

echo "# Converting $1 to Python..."

cat << EOF
T, P, C = {}, 0, 0

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

	    
EOF

sed "s/[^][]//g;s/\[/pico\(/g;s/]/),/g" ${1:-/dev/stdin}
