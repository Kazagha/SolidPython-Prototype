#! /usr/bin/env python3
import sys

from solid import scad_render_to_file
from solid.objects import cube, cylinder, difference, translate, union
from solid.utils import right

SEGMENTS = 48

def basic_geometry():

    right_piece = right(15)(cube([100, 50, 33], center=True))
    cyl = cylinder(r=75, h=50, center=True) - cylinder(r=65, h=50, center=True)
    right_piece += right(100)(cyl)

    return right_piece;

if __name__ == '__main__':
    out_dir = sys.argv[1] if len(sys.argv) > 1 else None
    print(f"this is a test" + out_dir)

    a = basic_geometry();

    file_out = scad_render_to_file(a,out_dir, file_header=f'$fn = {SEGMENTS};')
    print(f"{__file__}: SCAD file written to: \n{file_out}")