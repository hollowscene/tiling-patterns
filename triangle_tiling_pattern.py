# -*- coding: utf-8 -*-
"""
Simple Triangle Tiling Pattern Generator.

@author: Andrew Ting
@last-modified: 2022/07/09
"""


# %% Imports

import cairo

from bitlist_generator import generate_random_bitlist


# %% Functions

def generate_triangle_tiling(tile_dimensions: list,
                             tiling_dimensions: list,
                             colour_palette: list,
                             colour_picker: list,
                             ) -> cairo.ImageSurface:
    """Generate a triangle tiling pattern.

    Parameters
    ----------
    tile_dimensions : list
        Width, height of tiles (in pixels).
    tiling_dimensions : list
        Number of tiles across, number of tiles down.
    colour_palette : list
        List of RGB codes to randomly choose from.
    colour_picker : list
        Bitlist instructing which colour from colour_palette to choose.

    Returns
    -------
    surface : cairo.ImageSurface
        A cairo ImageSurface object which can be saved as a .png.

    """
    tile_width, tile_height = tile_dimensions
    n_tiles_across, n_tiles_down = tiling_dimensions

    assert len(colour_picker) == 2 * n_tiles_across * n_tiles_down

    width_px = tile_width * n_tiles_across
    height_px = tile_height * n_tiles_down

    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width_px, height_px)
    ctx = cairo.Context(surface)

    pointer_x = 0
    pointer_y = 0

    counter = 0

    for _ in range(n_tiles_down):
        for _ in range(n_tiles_across):
            # Draw the top triangle
            r, g, b = colour_palette[colour_picker[counter]]
            ctx.set_source_rgb(r, g, b)
            ctx.move_to(pointer_x, pointer_y)

            ctx.line_to(pointer_x + tile_width, pointer_y)
            ctx.line_to(pointer_x, pointer_y + tile_height)
            ctx.line_to(pointer_x, pointer_y)
            ctx.fill()
            counter += 1

            # Draw the bottom triangle
            r, g, b = colour_palette[colour_picker[counter]]
            ctx.set_source_rgb(r, g, b)
            ctx.move_to(pointer_x + tile_width, pointer_y)

            ctx.line_to(pointer_x + tile_width, pointer_y + tile_height)
            ctx.line_to(pointer_x, pointer_y + tile_height)
            ctx.line_to(pointer_x + tile_width, pointer_y)
            ctx.fill()
            counter += 1

            pointer_x += tile_width

        pointer_x = 0
        pointer_y += tile_height

    return surface


# %% Testing

if __name__ == "__main__":
    colour_palette = [(0.25, 0.2, 0.8), (0.8, 0.8, 0.9), (0.1, 0.1, 0.15)]
    tile_dimensions = [300, 200]
    tiling_dimensions = [10, 8]

    bitlist_length = 2 * tiling_dimensions[0] * tiling_dimensions[1]
    bitlist = generate_random_bitlist(bitlist_length, 3)

    surface = generate_triangle_tiling(tile_dimensions, tiling_dimensions,
                                       colour_palette, bitlist)

    # Unfortunately there are gaps between the triangles. I believe this is
    # because the vector shapes need to be rasterised when converted to .png

    # Writing this up to output as an .svg instead might fix this
    surface.write_to_png("10x8-triangle-tiling-pattern.png")
