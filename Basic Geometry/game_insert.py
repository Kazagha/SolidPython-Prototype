#! /usr/bin/env python3
import sys

from solid import scad_render_to_file
from solid.objects import cube, cylinder, difference, translate, union
from solid.utils import right,left,up,down,minkowski

SEGMENTS = 48

def game_insert():

    length, width, height = 150,100,50
    # Wall Thickness
    wall = 3
    wells = 2
    double_wall = wall*2

    box = roundbox([length,width,height],2)
    #insert = roundbox([length-double_wall,width-double_wall,height],2)
    well_size = [(length - (wall * (wells + 1))) / wells,width-double_wall,height]

    for i in range(wells):
        # Create the insert
        insert = roundbox(well_size,2)
        # Offset the insert
        insert = translate([wall * (i + 1) + well_size[0] * i,wall,wall])(insert)
        # Add the well into the box
        box -= insert

    return box

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

