#! /usr/bin/env python3
import sys

from solid import scad_render_to_file
from solid.objects import cube, cylinder, difference, translate, union
from solid.utils import right,left,up,down,minkowski

SEGMENTS = 48

def game_insert():

    length, width, height = 100,150,50
    # Wall Thickness
    wall = 5
    double_wall = wall*2

    box = (cube([length,width,height]))
    inner_box = (cube([length-double_wall,width-double_wall,height]))
    # Offset the Inner Box
    inner_box = translate([wall,wall,wall])(inner_box)
    insert = roundbox([length-double_wall,width-double_wall,height],2)
    # Offset the insert
    insert = translate([wall,wall,wall])(insert)
    return box - insert

def roundbox(size, radius):
    """"box with rounded edges."""

    x,y,z = size
    x = x - radius * 2
    y = y - radius * 2
    z = z - 1

    round_box = minkowski()(cube([x,y,z]))(cylinder(r=radius))
    round_box = translate([radius,radius,0])(round_box)

    return round_box

if __name__ == '__main__':
    out_dir = sys.argv[1] if len(sys.argv) > 1 else None
    print(f"this is a test" + out_dir)

    a = game_insert();

    file_out = scad_render_to_file(a,out_dir, file_header=f'$fn = {SEGMENTS};')
    print(f"{__file__}: SCAD file written to: \n{file_out}")

