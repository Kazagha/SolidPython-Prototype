#! /usr/bin/env python3
import sys

from solid import scad_render_to_file
from solid.objects import cube, cylinder, difference, translate, union, hull, rotate, circle
from solid.utils import right,left,up,down,minkowski, arc, linear_extrude, scale, intersection
from math import sin,cos,floor,sqrt,pow, radians,pi,fabs

SEGMENTS = 48

def Create_Hex(radius, wall_height, hex_wall):
    hex_wall = 3

    hex = (cylinder(r=radius, h=wall_height, segments=6))
    hex_insert = translate([0,0,-1])(cylinder(r=radius - hex_wall, h=wall_height + 2, segments=6))
    hex -= hex_insert

    return hex

def Hex_Wall():
    # Variables
    hex_wall = 3
    wall_length = 6 * 2.54 * 10
    wall_height = 2 * 2.54 * 10
    barrier_thickness = 10

    # Calculated Variables
    hex_radius = wall_height / 3
    hex_number = floor(wall_length / hex_radius)
    segment = 360 / 6
    # Calculate the length of the flat side (along the bottom of the hexagon)
    # a^2 = b^2 + c^2 - 2bc cosA
    side_length = sqrt(pow(hex_radius,2) + pow(hex_radius,2) - (2 * hex_radius * hex_radius * cos(radians(segment))))
    # Calculate the distance from the centre to the flat bottom of the hex
    # a^2 = b^2 + c^2 - rearranged
    #distance_to_side = sqrt(pow(hex_radius,2) - pow(side_length / 2,2))
    distance_to_side = hex_radius * cos(radians(segment / 2))
    # Calculate the X offset
    x_offset = (side_length / 2 + hex_radius)

    # Create the hexes
    hex = Create_Hex(radius=hex_radius, wall_height=barrier_thickness, hex_wall=hex_wall)
    hex += translate([x_offset, distance_to_side, 0])(hex)

    return hex

if __name__ == '__main__':
    out_dir = sys.argv[1] if len(sys.argv) > 1 else None
    print(f"this is a test" + out_dir)

    a = Hex_Wall();

    file_out = scad_render_to_file(a,out_dir, file_header=f'$fn = {SEGMENTS};')
    print(f"{__file__}: SCAD file written to: \n{file_out}")