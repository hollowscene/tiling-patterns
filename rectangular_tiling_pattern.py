# -*- coding: utf-8 -*-
"""
Simple Rectangle Tiling Pattern Generator.

@author: Andrew Ting
@last-modified: 2022/07/09
"""


# %% Imports

import cairo
import random

from bitlist_generator import generate_random_bitlist


# %% Functions

def generate_rectangle_tiling(tile_dimensions: list,
                              tiling_dimensions: list,
                              colour_palette: list = None,
                              colour_picker: list = None,
                              ) -> cairo.ImageSurface:
    """Generate a rectangle tiling pattern.

    Parameters
    ----------
    tile_dimensions : list
        Width, height of tiles (in pixels).
    tiling_dimensions : list
        Number of tiles across, number of tiles down.
    colour_palette : list, optional
        List of RGB codes to randomly choose from. If not given then choose
        3 uniformly random R, G and B values.
    colour_picker : list, optional
        Bitlist instructing which colour from colour_palette to choose. If
        colour_palette is None then colour_picker should also be None.

    Returns
    -------
    surface : cairo.ImageSurface
        A cairo ImageSurface object which can be saved as a .png.

    """
    assert not ((colour_palette is None) ^ (colour_picker is None))

    tile_width, tile_height = tile_dimensions
    n_tiles_across, n_tiles_down = tiling_dimensions

    if colour_picker is not None:
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
            if colour_palette is None:
                r = random.random()
                g = random.random()
                b = random.random()
            else:
                r, g, b = colour_palette[colour_picker[counter]]

            # Draw rectangle
            ctx.set_source_rgb(r, g, b)
            ctx.rectangle(pointer_x, pointer_y, tile_width, tile_height)
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

    surface = generate_rectangle_tiling(tile_dimensions, tiling_dimensions,
                                        colour_palette, bitlist)

    surface.write_to_png("10x8-rectangle-tiling-pattern.png")

    surface = generate_rectangle_tiling(tile_dimensions, tiling_dimensions)

    surface.write_to_png("10x8-rectangle-tiling-pattern-random.png")
