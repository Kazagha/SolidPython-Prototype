#! /usr/bin/env python3
import sys

from solid import scad_render_to_file
from solid.objects import cube, cylinder, difference, translate, union, hull, rotate
from solid.utils import right,left,up,down,minkowski
from math import sin,cos,floor

SEGMENTS = 48

def knurl():
    radius = 75
    height = 10
    knurl_segments = 48
    knurl_count = int(floor(knurl_segments / 2))

    box_lid = (cylinder(r=radius, h=height))

    # Circumference of the circle divided by number of segments
    # with a 1.5 multiplier to make the the knurl larger
    knurl_diameter = (3.14 * radius * 2) / knurl_segments * 1.5
    # Divide the circle evenly into segments, skipping every second segment
    knurl_step = 360 / knurl_segments * 2

    for i in range(knurl_count):
        knurl = (cylinder(d=knurl_diameter, h=height))
        # Push the knurl out 1 radius distance
        # Reduced slightly so the knurl is embedded
        knurl = (translate([radius - (knurl_diameter / 4) ,0,0]))(knurl)
        # Rotate the knurl into position around the circumference
        knurl = (rotate([0,0,i * knurl_step]))(knurl)
        box_lid += knurl

    return box_lid

if __name__ == '__main__':
    out_dir = sys.argv[1] if len(sys.argv) > 1 else None
    print(f"this is a test" + out_dir)

    a = knurl();

    file_out = scad_render_to_file(a,out_dir, file_header=f'$fn = {SEGMENTS};')
    print(f"{__file__}: SCAD file written to: \n{file_out}")