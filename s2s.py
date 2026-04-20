#! /usr/bin/env python3

from stl import mesh
import sys

def v2s(v):
    return '[' + (','.join([str(V) for V in v])) + ']'

m = mesh.Mesh.from_file(sys.argv[1])
for record in m.data:
    triangle = record[1]

    print('''
polyhedron(
    points = [''')
    print(v2s(triangle[0]) + ',')
    print(v2s(triangle[1]) + ',')
    print(v2s(triangle[2]))
    print('''],
    faces = [
        [0, 1, 2]
    ]
);''')
